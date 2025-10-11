
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { books } from "@/lib/books-data";
import Link from "next/link";
import { ArrowRight } from "lucide-react";

export default function BooksPage() {

  const getBookUrl = (book: (typeof books)[0]) => {
    switch (book.type) {
      case 'pdf':
        return `/books/view/${book.url}`;
      case 'multichapter':
        return `/books/${book.url}`;
      default:
        return book.url;
    }
  }

  return (
    <div className="container mx-auto px-4 md:px-6 py-12 md:py-24">
      <div className="text-center space-y-4 mb-12">
        <h1 className="text-4xl font-bold tracking-tighter sm:text-5xl md:text-6xl">Cybersecurity Bookshelf</h1>
        <p className="max-w-[700px] mx-auto text-muted-foreground md:text-xl">
          A curated collection of essential books for aspiring and professional cybersecurity experts.
        </p>
      </div>

      <div className="grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
        {books.map((book) => (
          <Card key={book.id} className="flex flex-col overflow-hidden transition-all hover:shadow-glow hover:border-primary">
            <CardHeader className="p-6">
              <CardTitle className="text-xl mb-2">{book.title}</CardTitle>
            </CardHeader>
            <CardContent className="p-6 pt-0 flex-grow">
              <CardDescription>{book.description}</CardDescription>
            </CardContent>
            <CardFooter className="p-6 pt-0 flex flex-col items-start">
              <div className="flex flex-wrap gap-2 mb-4">
                {book.tags.map(tag => (
                  <Badge key={tag} variant="secondary">{tag}</Badge>
                ))}
              </div>
              <Button asChild className="w-full group mt-auto">
                <Link 
                  href={getBookUrl(book)} 
                >
                  Read More <ArrowRight className="ml-2 h-5 w-5 transition-transform group-hover:translate-x-1" />
                </Link>
              </Button>
            </CardFooter>
          </Card>
        ))}
      </div>
    </div>
  );
}
