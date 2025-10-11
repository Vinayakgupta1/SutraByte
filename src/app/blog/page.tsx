import { Card, CardContent, CardDescription, CardFooter, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import Link from "next/link";
import { ArrowRight } from "lucide-react";
import { Button } from "@/components/ui/button";
import { blogPosts } from "@/lib/blog-data";

export default function BlogPage() {
  return (
    <div className="container mx-auto px-4 md:px-6 py-12 md:py-24">
      <div className="text-center space-y-4 mb-12">
        <h1 className="text-4xl font-bold tracking-tighter sm:text-5xl md:text-6xl">SutraByte Blog</h1>
        <p className="max-w-[700px] mx-auto text-muted-foreground md:text-xl">
          Stay updated with the latest trends, insights, and news in the cybersecurity world.
        </p>
      </div>

      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        {blogPosts.map((post) => (
          <Card key={post.title} className="flex flex-col overflow-hidden transition-all hover:shadow-glow hover:border-primary">
            <CardContent className="p-6 flex-grow">
              <div className="mb-2">
                {post.tags.map(tag => <Badge key={tag} variant="secondary" className="mr-2 mb-2">{tag}</Badge>)}
              </div>
              <CardTitle className="mb-2 text-xl">{post.title}</CardTitle>
              <CardDescription>{post.excerpt}</CardDescription>
            </CardContent>
            <CardFooter className="p-6 pt-0 flex justify-between items-center">
              <span className="text-sm text-muted-foreground">{post.date}</span>
              <Button asChild variant="link" className="group">
                <Link href={post.url} target="_blank" rel="noopener noreferrer">
                  Read More <ArrowRight className="ml-2 h-4 w-4 transition-transform group-hover:translate-x-1" />
                </Link>
              </Button>
            </CardFooter>
          </Card>
        ))}
      </div>
    </div>
  );
}
