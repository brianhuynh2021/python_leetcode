# DropBox Mini - Distributed File Storage System

A simplified Dropbox clone built with microservices architecture for learning system design concepts.

## 🏗️ Architecture

```
┌─────────────┐
│   Client    │ (Desktop/Mobile/Web)
│  (Watcher)  │
└──────┬──────┘
       │
       ↓
┌─────────────────────────────────────┐
│        Load Balancer (NGINX)        │
└─────────────────────────────────────┘
       │
       ↓
┌─────────────────────────────────────┐
│         API Gateway / Auth          │
└─────────────────────────────────────┘
       │
       ├─────────────┬──────────────┬──────────────┐
       ↓             ↓              ↓              ↓
┌─────────────┐ ┌──────────┐ ┌──────────┐ ┌────────────┐
│   Metadata  │ │  Upload  │ │ Download │ │  Sync      │
│   Service   │ │  Service │ │ Service  │ │  Service   │
└─────────────┘ └──────────┘ └──────────┘ └────────────┘
       │             │              │              │
       ↓             ↓              ↓              ↓
┌─────────────┐ ┌──────────────────────────────────────┐
│  PostgreSQL │ │        Object Storage (MinIO/S3)     │
│   + Redis   │ └──────────────────────────────────────┘
└─────────────┘
```

## 🚀 Features

- **File Upload/Download** - Chunked uploads with resume capability
- **File Sync** - Real-time synchronization across devices
- **File Versioning** - Keep history of file changes
- **Deduplication** - Save storage by detecting duplicate files
- **File Sharing** - Share files with other users
- **Authentication** - JWT-based secure authentication

## 📋 System Design Highlights

### Functional Requirements
✅ Upload/Download files
✅ File synchronization
✅ File sharing
✅ File versioning

### Non-Functional Requirements
✅ Scalability - Microservices architecture
✅ Reliability - Data redundancy with S3/MinIO
✅ Performance - Chunked transfer & CDN-ready
✅ Security - JWT authentication & encrypted storage

### Key Design Decisions

1. **Chunking Strategy** (4MB chunks)
   - Resume failed uploads
   - Parallel upload/download
   - Efficient delta sync

2. **Deduplication**
   - File-level hash checking
   - Shared storage for duplicate files

3. **Sync Algorithm**
   - Delta sync (only changed files)
   - WebSocket for real-time updates
   - Conflict resolution (last-write-wins)

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL
- **Cache**: Redis
- **Storage**: MinIO (S3-compatible)
- **Client**: Python (watchdog)
- **Container**: Docker & Docker Compose

## 📦 Project Structure

```
dropbox-mini/
├── services/
│   ├── auth_service/          # Authentication & JWT
│   ├── metadata_service/      # File metadata management
│   ├── upload_service/        # File upload with chunking
│   ├── download_service/      # File download
│   └── sync_service/          # File synchronization
├── client/
│   └── file_watcher.py        # Desktop client with auto-sync
├── common/
│   ├── config.py              # Shared configuration
│   ├── database.py            # Database setup
│   ├── models.py              # SQLAlchemy models
│   └── s3_client.py           # S3/MinIO client
├── alembic/                   # Database migrations
├── docker-compose.yml         # Service orchestration
└── requirements.txt
```

## 🚀 Quick Start

### 1. Setup Environment

```bash
# Copy environment file
cp .env.example .env

# Install dependencies
pip install -r requirements.txt
```

### 2. Start Services

```bash
# Start all services with Docker Compose
docker-compose up -d

# Check services are running
docker-compose ps
```

### 3. Run Database Migrations

```bash
# Apply migrations
alembic upgrade head
```

### 4. Test the API

```bash
# Register a user
curl -X POST http://localhost:8001/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "password123",
    "name": "Test User"
  }'

# Login and get token
curl -X POST http://localhost:8001/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@example.com&password=password123"
```

### 5. Run Client (File Watcher)

```bash
# Set environment variables
export DROPBOX_TOKEN="your-jwt-token"
export WATCH_FOLDER="./dropbox_sync"
export DROPBOX_API_URL="http://localhost:8003"

# Run file watcher
python client/file_watcher.py
```

## 📡 Service Endpoints

| Service | Port | Endpoint |
|---------|------|----------|
| Auth Service | 8001 | `/register`, `/token`, `/me` |
| Metadata Service | 8002 | `/files`, `/files/{id}` |
| Upload Service | 8003 | `/upload/init`, `/upload/chunk` |
| Download Service | 8004 | `/download/{id}` |
| Sync Service | 8005 | `/sync/delta`, `/ws/sync` |

## 🔑 API Examples

### Upload File

```python
import requests
import hashlib

# 1. Calculate file hash
with open('file.pdf', 'rb') as f:
    file_hash = hashlib.sha256(f.read()).hexdigest()

# 2. Initialize upload
response = requests.post(
    'http://localhost:8003/upload/init',
    headers={'Authorization': f'Bearer {token}'},
    json={
        'file_name': 'file.pdf',
        'file_size': 1024000,
        'file_hash': file_hash
    }
)

# 3. Upload chunks
# ... (see upload_service for details)
```

### Download File

```python
response = requests.get(
    f'http://localhost:8004/download/{file_id}',
    headers={'Authorization': f'Bearer {token}'},
    stream=True
)

with open('downloaded_file.pdf', 'wb') as f:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)
```

## 🎯 Learning Objectives

This project demonstrates:

1. **Microservices Architecture** - Service decomposition & communication
2. **Scalability Patterns** - Horizontal scaling, load balancing
3. **Data Management** - Chunking, deduplication, versioning
4. **Real-time Sync** - WebSocket, polling strategies
5. **Storage Optimization** - S3/MinIO, CDN integration
6. **Database Design** - Schema design, indexing, sharding concepts

## 🧪 Testing

```bash
# Unit tests
pytest tests/

# Integration tests
pytest tests/integration/

# Load testing
locust -f tests/load_test.py
```

## 📈 Scaling Considerations

### Database Sharding
- Shard by `user_id` for horizontal scaling
- Read replicas for metadata queries

### Caching Strategy
- Redis for metadata caching
- CDN for file downloads

### Load Balancing
- NGINX for API gateway
- Service mesh for inter-service communication

## 🔐 Security

- JWT-based authentication
- HTTPS for all communications
- S3 presigned URLs for secure downloads
- Rate limiting (TODO)

## 📝 Future Enhancements

- [ ] File encryption at rest
- [ ] Multi-region replication
- [ ] Collaborative editing
- [ ] Mobile apps (iOS/Android)
- [ ] Advanced conflict resolution
- [ ] Audit logs & analytics

## 📚 References

- [Designing Data-Intensive Applications](https://dataintensive.net/)
- [System Design Interview - Alex Xu](https://www.amazon.com/System-Design-Interview-insiders-Second/dp/B08CMF2CQF)
- [Dropbox System Design](https://github.com/donnemartin/system-design-primer#design-dropbox)

## 📄 License

MIT License - Feel free to use for learning!

---

**Built for learning System Design concepts** 🎓
