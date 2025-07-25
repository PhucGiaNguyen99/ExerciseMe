class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12))
    description = db.Column(db.String(18))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    exercises = db.relationship("Exercise")

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    weight = db.Column(db.Float(5))
    details = db.Column(db.String(5))
    include_details = db.Column(db.Boolean)
    workout_id = db.Column(db.Integer, db.ForeignKey("workout.id"))