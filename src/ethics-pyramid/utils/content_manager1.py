# src/ethics_pyramid/utils/content_manager.py

from pathlib import Path
import json
import shutil
import datetime
from typing import Dict, Any, Optional

class ContentManager:
    def __init__(self, root_dir: str = "quantum_storage"):
        self.root_dir = Path(root_dir)
        self.active_dir = self.root_dir / "active"
        self.archive_dir = self.root_dir / "archive"
        self.temp_dir = self.root_dir / "temp"
        
        # Create directory structure
        for directory in [self.active_dir, self.archive_dir, self.temp_dir]:
            directory.mkdir(parents=True, exist_ok=True)
            
    def store_content(self, content_id: str, content: Dict[str, Any], 
                     category: str = "default") -> bool:
        """Store content with quantum-runic signature and metadata"""
        try:
            timestamp = datetime.datetime.now().isoformat()
            content_package = {
                "content": content,
                "metadata": {
                    "quantum_signature": "ᚲᚹᚨᚾᛏᚢᛗ-∞",
                    "timestamp": timestamp,
                    "category": category,
                    "version": "1.0",
                    "id": content_id
                }
            }
            
            file_path = self.active_dir / category / f"{content_id}.json"
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(file_path, 'w') as f:
                json.dump(content_package, f, indent=2)
            return True
        except Exception as e:
            print(f"Error storing content: {e}")
            return False
            
    def archive_content(self, content_id: str, category: str = "default") -> bool:
        """Move content to archive with compression"""
        try:
            source = self.active_dir / category / f"{content_id}.json"
            if not source.exists():
                return False
                
            # Create archive structure
            archive_path = self.archive_dir / category / datetime.datetime.now().strftime("%Y%m")
            archive_path.mkdir(parents=True, exist_ok=True)
            
            # Move file to archive
            shutil.move(str(source), str(archive_path / f"{content_id}.json"))
            return True
        except Exception as e:
            print(f"Error archiving content: {e}")
            return False
            
    def retrieve_content(self, content_id: str, category: str = "default", 
                        include_archived: bool = False) -> Optional[Dict[str, Any]]:
        """Retrieve content from active or archived storage"""
        # Check active content first
        active_path = self.active_dir / category / f"{content_id}.json"
        if active_path.exists():
            with open(active_path) as f:
                return json.load(f)
                
        # Check archives if requested
        if include_archived:
            for archive_month in self.archive_dir.glob(f"{category}/*"):
                archive_path = archive_month / f"{content_id}.json"
                if archive_path.exists():
                    with open(archive_path) as f:
                        return json.load(f)
        
        return None
        
    def bulk_archive(self, category: str = "default", older_than_days: int = 30) -> int:
        """Archive content older than specified days"""
        count = 0
        cutoff = datetime.datetime.now() - datetime.timedelta(days=older_than_days)
        
        for content_file in (self.active_dir / category).glob("*.json"):
            with open(content_file) as f:
                content = json.load(f)
                timestamp = datetime.datetime.fromisoformat(
                    content["metadata"]["timestamp"]
                )
                
            if timestamp < cutoff:
                if self.archive_content(content["metadata"]["id"], category):
                    count += 1
                    
        return count