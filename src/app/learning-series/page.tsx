import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { CheckCircle2, Lock, Newspaper, Youtube } from "lucide-react";
import { Button } from "@/components/ui/button";
import { learningSeriesModules } from "@/lib/learning-series-data";
import Link from "next/link";

export default function LearningSeriesPage() {
  const modules = learningSeriesModules;
  const completedModules = modules.filter(m => m.completed).length;
  const progressPercentage = (completedModules / modules.length) * 100;

  return (
    <div className="container mx-auto px-4 md:px-6 py-12 md:py-24">
      <div className="text-center space-y-4 mb-12">
        <h1 className="text-4xl font-bold tracking-tighter sm:text-5xl md:text-6xl">45-Day Learning Series</h1>
        <p className="max-w-[700px] mx-auto text-muted-foreground md:text-xl">
          Your structured path to becoming a cybersecurity expert. Complete daily modules to build your knowledge from the ground up.
        </p>
      </div>

      <div className="max-w-3xl mx-auto mb-12">
        <Card>
          <CardHeader>
            <CardTitle>Your Progress</CardTitle>
            <CardDescription>{completedModules} of {modules.length} modules completed.</CardDescription>
          </CardHeader>
          <CardContent>
            <Progress value={progressPercentage} className="w-full" />
          </CardContent>
        </Card>
      </div>

      <div className="max-w-3xl mx-auto space-y-4">
        {modules.map((module) => (
          <Card key={module.day} className={`transition-all ${module.locked ? 'bg-muted/50' : 'hover:border-primary/50'}`}>
            <CardContent className="p-4 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
              <div className="flex items-center gap-4 flex-grow">
                <div className={`flex items-center justify-center h-12 w-12 rounded-full text-lg font-bold shrink-0 ${module.completed ? 'bg-green-600 text-white' : module.locked ? 'bg-gray-500 text-gray-300' : 'bg-primary text-primary-foreground'}`}>
                  {module.completed ? <CheckCircle2 /> : module.day}
                </div>
                <div className="flex-grow">
                  <h3 className="font-semibold">{`Day ${module.day}: ${module.title}`}</h3>
                  <p className="text-sm text-muted-foreground mt-1">
                    {module.description}
                  </p>
                </div>
              </div>
              <div className="flex items-center gap-2 mt-4 sm:mt-0 sm:ml-4 shrink-0 flex-wrap justify-start sm:justify-end">
                {module.blogUrl && (
                  <Button asChild size="sm" variant="outline">
                    <Link href={module.blogUrl} target="_blank"><Newspaper className="h-4 w-4 mr-2" /> Blog</Link>
                  </Button>
                )}
                {module.videoUrl && (
                   <Button asChild size="sm" variant="outline">
                    <Link href={module.videoUrl} target="_blank"><Youtube className="h-4 w-4 mr-2" /> Video</Link>
                  </Button>
                )}
                <Button size="sm" disabled={module.locked || module.completed}>
                  {module.completed ? 'Completed' : module.locked ? <Lock className="h-4 w-4" /> : 'Upcoming'}
                </Button>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}
