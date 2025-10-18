
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { roadmaps } from "@/lib/roadmaps-data";
import Link from "next/link";
import { ArrowRight } from "lucide-react";

export default function RoadmapsPage() {

  const getRoadmapUrl = (roadmap: (typeof roadmaps)[0]) => {
    switch (roadmap.type) {
      case 'pdf':
        return `/roadmaps/view/${roadmap.url}`;
      case 'markdown':
        return `/roadmaps/${roadmap.url}`;
      default:
        return `/roadmaps/${roadmap.url}`;
    }
  }

  return (
    <div className="container mx-auto px-4 md:px-6 py-12 md:py-24">
      <div className="text-center space-y-4 mb-12">
        <h1 className="text-4xl font-bold tracking-tighter sm:text-5xl md:text-6xl">Cybersecurity Roadmaps</h1>
        <p className="max-w-[700px] mx-auto text-muted-foreground md:text-xl">
          Structured learning paths to guide your cybersecurity career journey.
        </p>
      </div>

      <div className="grid md:grid-cols-1 lg:grid-cols-2 gap-8 max-w-4xl mx-auto">
        {roadmaps.map((roadmap) => (
          <Card key={roadmap.id} className="flex flex-col overflow-hidden transition-all hover:shadow-glow hover:border-primary">
            <CardHeader className="p-6">
              <CardTitle className="text-xl mb-2">{roadmap.title}</CardTitle>
            </CardHeader>
            <CardContent className="p-6 pt-0 flex-grow">
              <CardDescription>{roadmap.description}</CardDescription>
            </CardContent>
            <CardFooter className="p-6 pt-0 flex flex-col items-start">
              <div className="flex flex-wrap gap-2 mb-4">
                {roadmap.tags.map(tag => (
                  <Badge key={tag} variant="secondary">{tag}</Badge>
                ))}
              </div>
              <Button asChild className="w-full group mt-auto">
                <Link href={getRoadmapUrl(roadmap)}>
                  View Roadmap <ArrowRight className="ml-2 h-5 w-5 transition-transform group-hover:translate-x-1" />
                </Link>
              </Button>
            </CardFooter>
          </Card>
        ))}
      </div>
    </div>
  );
}
