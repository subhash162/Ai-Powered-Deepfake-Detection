from sqlalchemy.orm import Session # type: ignore
from typing import List, Optional
from datetime import datetime
from app.models.detection import Detection
from app.schemas.detection import DetectionCreate, DetectionUpdate

def create_detection(db: Session, detection: DetectionCreate, user_id: int) -> Detection:
    db_detection = Detection(
        user_id=user_id,
        image_path=detection.image_path,
        image_name=detection.image_name,
        image_size=detection.image_size
    )
    db.add(db_detection)
    db.commit()
    db.refresh(db_detection)
    return db_detection

def get_detection(db: Session, detection_id: int) -> Optional[Detection]:
    return db.query(Detection).filter(Detection.id == detection_id).first()

def get_user_detections(
    db: Session, 
    user_id: int, 
    skip: int = 0, 
    limit: int = 100
) -> List[Detection]:
    return db.query(Detection)\
        .filter(Detection.user_id == user_id)\
        .order_by(Detection.created_at.desc())\
        .offset(skip)\
        .limit(limit)\
        .all()

def get_detections_count(db: Session, user_id: int) -> int:
    return db.query(Detection).filter(Detection.user_id == user_id).count()

def update_detection(
    db: Session, 
    detection_id: int, 
    detection_update: DetectionUpdate
) -> Optional[Detection]:
    db_detection = get_detection(db, detection_id)
    if not db_detection:
        return None
    
    update_data = detection_update.dict(exclude_unset=True)
    if update_data:
        update_data["processed_at"] = datetime.utcnow()
    
    for key, value in update_data.items():
        setattr(db_detection, key, value)
    
    db.commit()
    db.refresh(db_detection)
    return db_detection

def delete_detection(db: Session, detection_id: int) -> bool:
    db_detection = get_detection(db, detection_id)
    if not db_detection:
        return False
    db.delete(db_detection)
    db.commit()
    return True