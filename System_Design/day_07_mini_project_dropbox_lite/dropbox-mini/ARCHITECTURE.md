# DropBox Mini - System Architecture Diagrams

## 1. High-Level Architecture

```mermaid
graph TB
    subgraph "Client Layer"
        Client1[Desktop Client]
        Client2[Web Client]
        Client3[Mobile Client]
    end
    
    subgraph "API Gateway Layer"
        LB[Load Balancer<br/>NGINX]
        Auth[Auth Service<br/>:8001]
    end
    
    subgraph "Service Layer"
        Meta[Metadata Service<br/>:8002]
        Upload[Upload Service<br/>:8003]
        Download[Download Service<br/>:8004]
        Sync[Sync Service<br/>:8005]
    end
    
    subgraph "Data Layer"
        DB[(PostgreSQL<br/>Metadata DB)]
        Cache[(Redis<br/>Cache)]
        Storage[(MinIO/S3<br/>Object Storage)]
    end
    
    Client1 --> LB
    Client2 --> LB
    Client3 --> LB
    
    LB --> Auth
    Auth --> Meta
    Auth --> Upload
    Auth --> Download
    Auth --> Sync
    
    Meta --> DB
    Meta --> Cache
    Upload --> DB
    Upload --> Storage
    Download --> DB
    Download --> Storage
    Sync --> DB
    Sync --> Cache
    
    style Auth fill:#ff9999
    style Meta fill:#99ccff
    style Upload fill:#99ff99
    style Download fill:#ffcc99
    style Sync fill:#cc99ff
```

## 2. File Upload Flow

```mermaid
sequenceDiagram
    actor User
    participant Client
    participant Auth
    participant Upload
    participant DB
    participant S3
    
    User->>Client: Select File
    Client->>Client: Calculate SHA-256 Hash
    Client->>Auth: Login Request
    Auth-->>Client: JWT Token
    
    Client->>Upload: POST /upload/init<br/>{file_name, file_size, file_hash}
    Upload->>DB: Check if hash exists (Dedup)
    
    alt File Exists (Deduplication)
        DB-->>Upload: File found
        Upload->>DB: Create metadata reference
        Upload-->>Client: {deduplication: true}
    else New File
        Upload->>DB: Create file & version record
        Upload-->>Client: {version_id, chunk_size, num_chunks}
        
        loop For each chunk
            Client->>Client: Split file into chunks
            Client->>Upload: POST /upload/chunk<br/>{version_id, chunk_index, chunk_data}
            Upload->>Upload: Verify chunk hash
            Upload->>S3: Upload chunk
            Upload->>DB: Save chunk metadata
            Upload-->>Client: {uploaded: true}
        end
        
        Client->>Upload: POST /upload/complete/{version_id}
        Upload->>DB: Verify all chunks uploaded
        Upload->>DB: Update user storage
        Upload-->>Client: {status: completed}
    end
    
    Client->>User: Upload Complete ✓
```

## 3. File Download Flow

```mermaid
sequenceDiagram
    actor User
    participant Client
    participant Auth
    participant Download
    participant DB
    participant S3
    
    User->>Client: Request File Download
    Client->>Auth: Authenticate
    Auth-->>Client: JWT Token
    
    Client->>Download: GET /download/{file_id}
    Download->>DB: Get file metadata
    Download->>DB: Get latest version
    Download->>DB: Get all chunks (ordered)
    
    loop For each chunk
        Download->>S3: Download chunk
        S3-->>Download: Chunk data
        Download-->>Client: Stream chunk
    end
    
    Client->>Client: Reassemble file
    Client->>User: File Ready ✓
```

## 4. File Sync Flow

```mermaid
sequenceDiagram
    actor User
    participant Watcher as File Watcher
    participant Sync
    participant Upload
    participant Download
    participant DB
    
    User->>Watcher: Start File Watcher
    Watcher->>Watcher: Monitor folder changes
    
    rect rgb(200, 255, 200)
        Note over Watcher,Upload: Local Change → Upload
        Watcher->>Watcher: Detect file created/modified
        Watcher->>Upload: Upload file (chunked)
        Upload->>DB: Save metadata
        Upload->>Sync: Notify change
    end
    
    rect rgb(200, 220, 255)
        Note over Watcher,Download: Remote Change → Download
        loop Every 30 seconds
            Watcher->>Sync: GET /sync/delta?since={timestamp}
            Sync->>DB: Get files changed since timestamp
            Sync-->>Watcher: {changes: [...]}
            
            alt Has Changes
                Watcher->>Download: Download changed files
                Download-->>Watcher: File data
                Watcher->>Watcher: Save to local folder
            end
        end
    end
    
    rect rgb(255, 230, 200)
        Note over Watcher,Sync: Real-time via WebSocket
        Watcher->>Sync: WS Connect /ws/sync/{user_id}
        Sync-->>Watcher: {type: file_change, data: {...}}
        Watcher->>Download: Download immediately
    end
```

## 5. Database Schema

```mermaid
erDiagram
    USERS ||--o{ FILES : owns
    USERS ||--o{ SHARED_FILES : shares
    USERS ||--o{ SHARED_FILES : receives
    FILES ||--o{ FILE_VERSIONS : has
    FILES ||--o{ SHARED_FILES : shared_via
    FILE_VERSIONS ||--o{ FILE_CHUNKS : contains
    
    USERS {
        uuid user_id PK
        string email UK
        string name
        string password_hash
        bigint storage_used
        bigint storage_limit
        timestamp created_at
    }
    
    FILES {
        uuid file_id PK
        uuid user_id FK
        string file_name
        string file_path
        bigint file_size
        string file_type
        string file_hash
        boolean is_deleted
        timestamp created_at
        timestamp updated_at
    }
    
    FILE_VERSIONS {
        uuid version_id PK
        uuid file_id FK
        int version_number
        string storage_path
        string file_hash
        bigint file_size
        timestamp created_at
    }
    
    FILE_CHUNKS {
        uuid chunk_id PK
        uuid version_id FK
        int chunk_index
        string chunk_hash
        bigint chunk_size
        string storage_path
    }
    
    SHARED_FILES {
        uuid share_id PK
        uuid file_id FK
        uuid owner_id FK
        uuid shared_with_user_id FK
        string permission
        timestamp created_at
    }
```

## 6. Microservices Components

```mermaid
graph LR
    subgraph "Auth Service :8001"
        A1[Register User]
        A2[Login/JWT]
        A3[Verify Token]
        A4[Get User Info]
    end
    
    subgraph "Metadata Service :8002"
        M1[List Files]
        M2[Get File Info]
        M3[Delete File]
        M4[Update Metadata]
    end
    
    subgraph "Upload Service :8003"
        U1[Init Upload]
        U2[Upload Chunk]
        U3[Complete Upload]
        U4[Deduplication]
    end
    
    subgraph "Download Service :8004"
        D1[Download File]
        D2[Stream Chunks]
        D3[Generate URL]
    end
    
    subgraph "Sync Service :8005"
        S1[Get Delta]
        S2[WebSocket Sync]
        S3[Notify Changes]
    end
    
    style A1 fill:#ffcccc
    style A2 fill:#ffcccc
    style M1 fill:#ccddff
    style U1 fill:#ccffcc
    style D1 fill:#ffeecc
    style S1 fill:#ddccff
```

## 7. Data Flow - Chunking & Deduplication

```mermaid
flowchart TD
    Start([User Uploads File]) --> Hash[Calculate SHA-256 Hash]
    Hash --> Init[POST /upload/init]
    Init --> Check{Hash exists<br/>in DB?}
    
    Check -->|Yes| Dedup[Deduplication]
    Dedup --> Link[Create metadata link]
    Link --> Done1([Upload Complete<br/>No Storage Used])
    
    Check -->|No| Split[Split into 4MB Chunks]
    Split --> Loop{More chunks?}
    Loop -->|Yes| ChunkHash[Calculate Chunk Hash]
    ChunkHash --> Upload[Upload Chunk to S3]
    Upload --> SaveMeta[Save Chunk Metadata]
    SaveMeta --> Loop
    
    Loop -->|No| Verify[Verify All Chunks]
    Verify --> UpdateStorage[Update User Storage]
    UpdateStorage --> Done2([Upload Complete])
    
    style Dedup fill:#90EE90
    style Done1 fill:#90EE90
    style Done2 fill:#87CEEB
```

## 8. Scalability & Performance

```mermaid
graph TB
    subgraph "Client Tier"
        C1[Web Client]
        C2[Desktop Client]
        C3[Mobile Client]
    end
    
    subgraph "CDN Layer"
        CDN[CloudFlare CDN<br/>Static Files]
    end
    
    subgraph "Load Balancer Tier"
        LB1[NGINX LB 1]
        LB2[NGINX LB 2]
    end
    
    subgraph "Service Tier - Auto Scaling"
        Auth1[Auth Service 1]
        Auth2[Auth Service 2]
        Upload1[Upload Service 1]
        Upload2[Upload Service 2]
        Meta1[Metadata Service 1]
        Meta2[Metadata Service 2]
    end
    
    subgraph "Cache Tier"
        Redis1[(Redis Master)]
        Redis2[(Redis Replica)]
    end
    
    subgraph "Database Tier - Sharding"
        DB1[(PostgreSQL<br/>Shard 1<br/>user_id: 0-499)]
        DB2[(PostgreSQL<br/>Shard 2<br/>user_id: 500-999)]
        DBR1[(Read Replica 1)]
        DBR2[(Read Replica 2)]
    end
    
    subgraph "Storage Tier - Multi-Region"
        S3_US[(S3/MinIO<br/>US-East)]
        S3_EU[(S3/MinIO<br/>EU-West)]
        S3_ASIA[(S3/MinIO<br/>Asia-Pacific)]
    end
    
    C1 --> CDN
    C2 --> CDN
    C3 --> CDN
    CDN --> LB1
    CDN --> LB2
    
    LB1 --> Auth1
    LB1 --> Upload1
    LB2 --> Auth2
    LB2 --> Upload2
    
    Auth1 --> Redis1
    Auth2 --> Redis1
    Redis1 --> Redis2
    
    Meta1 --> DB1
    Meta2 --> DB2
    DB1 --> DBR1
    DB2 --> DBR2
    
    Upload1 --> S3_US
    Upload2 --> S3_EU
    
    style CDN fill:#FFD700
    style Redis1 fill:#FF6347
    style S3_US fill:#87CEEB
```

## 9. System Deployment

```mermaid
graph TB
    subgraph "Docker Compose Stack"
        subgraph "Network: dropbox-network"
            PG[PostgreSQL:5432]
            RD[Redis:6379]
            MN[MinIO:9000/9001]
            
            A[Auth Service:8001]
            M[Metadata Service:8002]
            U[Upload Service:8003]
            D[Download Service:8004]
            S[Sync Service:8005]
        end
    end
    
    subgraph "Volumes"
        V1[(postgres_data)]
        V2[(minio_data)]
    end
    
    A --> PG
    A --> RD
    M --> PG
    M --> RD
    U --> PG
    U --> MN
    D --> PG
    D --> MN
    S --> PG
    S --> RD
    
    PG -.-> V1
    MN -.-> V2
    
    style PG fill:#336791
    style RD fill:#DC382D
    style MN fill:#C72E49
```

## Key Metrics & SLA

| Metric | Target | Current |
|--------|--------|---------|
| **Availability** | 99.9% | - |
| **Upload Speed** | 50 MB/s | - |
| **Download Speed** | 100 MB/s | - |
| **Sync Latency** | < 2s | - |
| **API Response Time** | < 100ms (p95) | - |
| **Storage Dedup Rate** | > 30% | - |

## Technology Stack Summary

```mermaid
mindmap
  root((DropBox Mini))
    Backend
      FastAPI
      Python 3.11
      SQLAlchemy
      Alembic
    Database
      PostgreSQL
      Redis Cache
    Storage
      MinIO/S3
      Chunked Storage
    Authentication
      JWT
      OAuth2
      Bcrypt
    Infrastructure
      Docker
      Docker Compose
      NGINX
    Client
      Watchdog
      WebSocket
      HTTP Client
    Monitoring
      Prometheus
      Grafana
      ELK Stack
```

---

**Diagrams created with Mermaid** - Render in GitHub, VS Code, or any Markdown viewer with Mermaid support 📊
