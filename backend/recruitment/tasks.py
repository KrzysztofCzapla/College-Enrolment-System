from celery import shared_task


@shared_task()
def calculate_stage_results(stage_id: int):
    """
    1) Get all students for this stage
    1.5) Check how many places are left
    2) for every student:
    2.1) Check if student hasnt accepted other offers
    2.2) Check if student has the right exams
    2.3) Calculate student score
    2.4) Take as many student as many places are left
    2.5) Change each applications status
    2.6) Make it so when student accepts application it sets them as student for university and offer

    """

