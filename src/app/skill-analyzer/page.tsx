import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { SkillAnalyzerForm } from "./SkillAnalyzerForm";
import { Lightbulb } from "lucide-react";

export default function SkillAnalyzerPage() {
  return (
    <div className="container mx-auto px-4 md:px-6 py-12 md:py-24">
      <div className="max-w-3xl mx-auto">
        <Card className="overflow-hidden">
          <CardHeader className="bg-primary/10 text-center p-8">
            <div className="mx-auto bg-primary text-primary-foreground rounded-full h-16 w-16 flex items-center justify-center mb-4">
                <Lightbulb className="h-8 w-8" />
            </div>
            <CardTitle className="text-3xl font-bold">Cybersecurity Skill Analyzer</CardTitle>
            <CardDescription className="text-lg text-muted-foreground max-w-2xl mx-auto">
              Tell us about your current skills and future goals. Our AI will generate personalized learning recommendations to guide your journey.
            </CardDescription>
          </CardHeader>
          <CardContent className="p-6 md:p-8">
            <SkillAnalyzerForm />
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
