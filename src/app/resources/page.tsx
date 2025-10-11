import { Card, CardDescription, CardTitle } from "@/components/ui/card";
import Link from "next/link";
import { BookOpen, Terminal, BookMarked } from "lucide-react";

export default function ResourcesPage() {
  return (
    <div className="container mx-auto px-4 md:px-6 py-12 md:py-24">
      <div className="text-center space-y-4 mb-12">
        <h1 className="text-4xl font-bold tracking-tighter sm:text-5xl md:text-6xl">Resources Hub</h1>
        <p className="max-w-[700px] mx-auto text-muted-foreground md:text-xl">
          Your central place for all cybersecurity learning materials, from articles and tools to structured courses.
        </p>
      </div>

       <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8 mb-12 max-w-6xl mx-auto">
        <Link href="/learning-series">
          <Card className="h-full flex flex-col justify-center items-center text-center p-8 transition-all hover:shadow-glow hover:border-primary hover:-translate-y-1">
            <BookOpen className="h-12 w-12 text-primary mb-4" />
            <CardTitle className="text-2xl">Learning Series</CardTitle>
            <CardDescription>A 45-day structured program to build your expertise from the ground up.</CardDescription>
          </Card>
        </Link>
        <Link href="/tryhackme">
          <Card className="h-full flex flex-col justify-center items-center text-center p-8 transition-all hover:shadow-glow hover:border-primary hover:-translate-y-1">
            <Terminal className="h-12 w-12 text-primary mb-4" />
            <CardTitle className="text-2xl">TryHackMe Rooms</CardTitle>
            <CardDescription>Follow our curated list of TryHackMe rooms to practice your skills.</CardDescription>
          </Card>
        </Link>
         <Link href="/books">
          <Card className="h-full flex flex-col justify-center items-center text-center p-8 transition-all hover:shadow-glow hover:border-primary hover:-translate-y-1 md:col-span-2 lg:col-span-1">
            <BookMarked className="h-12 w-12 text-primary mb-4" />
            <CardTitle className="text-2xl">Books</CardTitle>
            <CardDescription>A curated collection of essential cybersecurity books and reading materials.</CardDescription>
          </Card>
        </Link>
      </div>
    </div>
  );
}
