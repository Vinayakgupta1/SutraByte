import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { ArrowRight } from "lucide-react";
import Link from "next/link";

export default function FeedbackPage() {
  return (
    <div className="container mx-auto px-4 md:px-6 py-12 md:py-24">
      <div className="max-w-2xl mx-auto">
        <Card>
          <CardHeader className="text-center">
            <CardTitle className="text-3xl font-bold">Submit Feedback</CardTitle>
            <CardDescription>
              We value your input! To leave feedback, please fill out our Google Form. Your
              responses help us improve.
            </CardDescription>
          </CardHeader>
          <CardContent className="text-center">
            <Button asChild size="lg" className="group">
                {/* Replace this with your actual Google Form link */}
                <Link href="https://docs.google.com/forms/d/e/1FAIpQLScw9gPAp3A3v2c-c5acT8TzU9Ie_t1g8y_Vp8oJ8a7B6d5w/viewform?usp=sf_link" target="_blank" rel="noopener noreferrer">
                    Go to Google Form <ArrowRight className="ml-2 h-5 w-5 transition-transform group-hover:translate-x-1" />
                </Link>
            </Button>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
