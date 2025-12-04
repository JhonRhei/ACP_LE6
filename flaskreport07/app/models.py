from app import db
from datetime import datetime

class Record(db.Model):
    
    # Table name (optional - auto-generated from class name)
    __tablename__ = 'records'
    
    # Columns: db.Column(type, constraints...)
    # Primary key: unique identifier for each row
    id = db.Column(db.Integer, primary_key=True)
    
    # String column with max length
    title = db.Column(db.String(140), nullable=False)
    
    # Text column (unlimited length)
    content = db.Column(db.Text)
    
    # DateTime with automatic default value
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Foreign key will be added in Stage 7 (authentication)
    # owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def __repr__(self):
        """String representation for debugging"""
        return f'<Record {self.id}: {self.title}>'
    
    def to_dict(self):
        """Convert model instance to dictionary (for JSON API)"""
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
