# In-Memory File System

The In-Memory File System is a Python program that simulates the behavior of a real file system, but all operations happen entirely in memory rather than on a physical disk. This system provides essential file system functionalities, such as:

- Creating directories and files
- Navigating between directories
- Listing files
- Reading and writing file contents
- Performing file operations like moving, copying, and deleting

### Documentation

For detailed documentation, please refer to the following link:
[In-Memory File System Documentation](https://docs.google.com/document/d/18mTw-96WIyoxFCPuLEvCF2Ug_9saY-JDS4HFDe5veBw/edit?usp=sharing)

### Project Structure:
```bash
├── src/
│   ├── core/           # Core file system components
│   ├── commands/       # Command implementations
│   ├── utils/          # Utility functions
│   └── cli/            # Command line interface
├── tests/              # Unit tests
└── main.py             # Entry point
```

## Requirements
- Python 3.8+

## Setup

### Clone the repository:
```bash
git clone https://github.com/Vineetttt/In-Memory-File-System.git
cd in-memory-file-system
```

### Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

### Running the Application:
```bash
python main.py
```

### Running Tests:
```bash
python -m unittest discover tests
```
