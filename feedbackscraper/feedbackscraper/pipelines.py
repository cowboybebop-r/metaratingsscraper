class FeedbackscraperPipeline:
    def process_item(self, item, spider):
        from main.models import Feedback
        feedback = Feedback()
        feedback.username = item.get('username', None)
        feedback.source = item.get('source', None)
        feedback.content = item.get('content', None)
        feedback.save()
        return item
