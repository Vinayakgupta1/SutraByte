import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { CheckCircle2, Lock, ArrowUpRight, Newspaper, Youtube } from "lucide-react";
import { Button } from "@/components/ui/button";
import { tryHackMeRooms } from "@/lib/tryhackme-data";
import Link from "next/link";
import { Badge } from "@/components/ui/badge";

export default function TryHackMePage() {
  const rooms = tryHackMeRooms;
  const completedRooms = rooms.filter(r => r.completed).length;
  const progressPercentage = (completedRooms / rooms.length) * 100;

  const getDifficultyBadge = (difficulty: 'Easy' | 'Medium' | 'Hard') => {
    switch (difficulty) {
      case 'Easy':
        return <Badge variant="secondary" className="bg-green-200 text-green-900 dark:bg-green-800 dark:text-green-100">Easy</Badge>;
      case 'Medium':
        return <Badge variant="secondary" className="bg-yellow-200 text-yellow-900 dark:bg-yellow-800 dark:text-yellow-100">Medium</Badge>;
      case 'Hard':
        return <Badge variant="secondary" className="bg-red-200 text-red-900 dark:bg-red-800 dark:text-red-100">Hard</Badge>;
    }
  };

  return (
    <div className="container mx-auto px-4 md:px-6 py-12 md:py-24">
      <div className="text-center space-y-4 mb-12">
        <h1 className="text-4xl font-bold tracking-tighter sm:text-5xl md:text-6xl">TryHackMe Pathway</h1>
        <p className="max-w-[700px] mx-auto text-muted-foreground md:text-xl">
          A curated list of TryHackMe rooms to practice your offensive and defensive security skills.
        </p>
      </div>

      <div className="max-w-3xl mx-auto mb-12">
        <Card>
          <CardHeader>
            <CardTitle>Your Progress</CardTitle>
            <CardDescription>{completedRooms} of {rooms.length} rooms completed.</CardDescription>
          </CardHeader>
          <CardContent>
            <Progress value={progressPercentage} className="w-full" />
          </CardContent>
        </Card>
      </div>

      <div className="max-w-3xl mx-auto space-y-4">
        {rooms.map((room) => (
          <Card key={room.id} className={`transition-all ${room.locked ? 'bg-muted/50' : 'hover:border-primary/50'}`}>
            <CardContent className="p-4 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
              <div className="flex items-center gap-4 flex-grow">
                 <div className={`flex items-center justify-center h-12 w-12 rounded-full text-lg font-bold shrink-0 ${room.completed ? 'bg-green-600 text-white' : room.locked ? 'bg-gray-500 text-gray-300' : 'bg-primary text-primary-foreground'}`}>
                  {room.completed ? <CheckCircle2 /> : room.id}
                </div>
                <div className="flex-grow">
                  <h3 className="font-semibold">{room.title}</h3>
                  <div className="flex items-center flex-wrap gap-2 mt-1">
                    {getDifficultyBadge(room.difficulty)}
                    <div className="flex flex-wrap gap-2">
                        {room.tags.map(tag => <Badge key={tag} variant="secondary">{tag}</Badge>)}
                    </div>
                  </div>
                </div>
              </div>
              <div className="flex flex-wrap items-center gap-2 mt-4 sm:mt-0 sm:ml-4 sm:shrink-0 justify-start sm:justify-end w-full sm:w-auto">
                {room.blogUrl && (
                  <Button asChild size="sm" variant="outline" disabled={room.locked}>
                    <Link href={room.blogUrl} target="_blank"><Newspaper className="h-4 w-4 mr-2" /> Blog</Link>
                  </Button>
                )}
                {room.videoUrl && (
                   <Button asChild size="sm" variant="outline" disabled={room.locked}>
                    <Link href={room.videoUrl} target="_blank"><Youtube className="h-4 w-4 mr-2" /> Video</Link>
                  </Button>
                )}
                <Button asChild size="sm" variant="outline" disabled={room.locked}>
                    <Link href={room.url} target="_blank">
                        View Room <ArrowUpRight className="h-4 w-4 ml-2" />
                    </Link>
                </Button>
                <Button size="sm" disabled={room.locked || room.completed}>
                  {room.completed ? 'Completed' : room.locked ? <Lock className="h-4 w-4" /> : 'Mark as Done'}
                </Button>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}
