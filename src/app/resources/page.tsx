import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import Link from "next/link";
import { BookOpen, Newspaper } from "lucide-react";

export default function ResourcesPage() {
  return (
    <div className="container mx-auto px-4 md:px-6 py-12 md:py-24">
      <div className="text-center space-y-4 mb-12">
        <h1 className="text-4xl font-bold tracking-tighter sm:text-5xl md:text-6xl">Resources Hub</h1>
        <p className="max-w-[700px] mx-auto text-muted-foreground md:text-xl">
          Your central place for all cybersecurity learning materials, from articles and tools to structured courses.
        </p>
      </div>

      <div className="grid md:grid-cols-2 gap-8 mb-12 max-w-4xl mx-auto">
        <Link href="/learning-series">
          <Card className="h-full flex flex-col justify-center items-center text-center p-8 transition-all hover:shadow-glow hover:border-primary hover:-translate-y-1">
            <BookOpen className="h-12 w-12 text-primary mb-4" />
            <CardTitle className="text-2xl">Learning Series</CardTitle>
            <CardDescription>A 45-day structured program to build your expertise from the ground up.</CardDescription>
          </Card>
        </Link>
        <Link href="/blog">
          <Card className="h-full flex flex-col justify-center items-center text-center p-8 transition-all hover:shadow-glow hover:border-primary hover:-translate-y-1">
            <Newspaper className="h-12 w-12 text-primary mb-4" />
            <CardTitle className="text-2xl">Blog</CardTitle>
            <CardDescription>Stay updated with the latest trends, insights, and news in the cybersecurity world.</CardDescription>
          </Card>
        </Link>
      </div>
    </div>
  );
}
