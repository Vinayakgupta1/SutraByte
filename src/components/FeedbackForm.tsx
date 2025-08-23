import { Button } from "./ui/button";

interface FeedbackFormProps {
  moduleTitle: string;
  moduleDay: number;
}

export function FeedbackForm({ moduleTitle, moduleDay }: FeedbackFormProps) {
  // Replace this URL with your Google Form URL
  const GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdszbm1iOUE8UWq9em2C03JjnzM_QKKaysNyqBoFkZXiR4m4Q/viewform?usp=header";

  const handleFeedbackClick = () => {
    // You can add pre-filled parameters to your Google Form URL
    const formUrl = `${GOOGLE_FORM_URL}?usp=pp_url&entry.123456789=${encodeURIComponent(moduleTitle)}&entry.987654321=${moduleDay}`;
    window.open(formUrl, '_blank');
  };

  return (
    <Button 
      onClick={handleFeedbackClick}
      className="mt-4"
      variant="outline"
    >
      Provide Feedback
    </Button>
  );
}