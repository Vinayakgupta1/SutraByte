
import { promises as fs } from 'fs';
import path from 'path';
import { notFound } from 'next/navigation';
import { books } from '@/lib/books-data';
import { Badge } from '@/components/ui/badge';
import Link from 'next/link';
import { Button } from '@/components/ui/button';
import { ArrowRight } from 'lucide-react';

type BookPageProps = {
  params: {
    slug: string;
  };
};

async function getBookDetails(slug: string) {
  const book = books.find((b) => b.url === slug);
  if (!book) {
    return null;
  }
  return { book };
}

export async function generateStaticParams() {
  return books
    .filter(book => book.type === 'multichapter')
    .map((book) => ({
      slug: book.url,
    }));
}

export default async function BookPage({ params }: BookPageProps) {
  const data = await getBookDetails(params.slug);

  if (!data) {
    notFound();
  }

  const { book } = data;

  if (book.type !== 'multichapter') {
      // This page is for multi-chapter books. 
      // Single markdown/pdf books are handled differently.
      notFound();
  }

  const chapterList = [];
  if (book.summary) {
    chapterList.push({ title: 'Summary Chapter', url: `./${params.slug}/summary` });
  }
  for (let i = 1; i <= (book.chapters || 0); i++) {
    chapterList.push({ title: `Project Chapter ${i}`, url: `./${params.slug}/chapter-${i}` });
  }

  return (
    <div className="container mx-auto px-4 md:px-6 py-12">
      <div className="max-w-4xl mx-auto">
        <div className="mb-12 text-center">
          <h1 className="text-4xl font-bold tracking-tighter sm:text-5xl md:text-6xl">{book.title}</h1>
          <p className="max-w-[700px] mx-auto text-muted-foreground md:text-xl mt-4">{book.description}</p>
          <div className="flex justify-center flex-wrap gap-2 mt-4">
            {book.tags.map(tag => (
              <Badge key={tag} variant="secondary">{tag}</Badge>
            ))}
          </div>
        </div>
        
        <div className="space-y-4">
            <h2 className="text-3xl font-bold text-center border-b pb-4">Table of Contents</h2>
            <ul className="divide-y divide-border">
                {chapterList.map((chapter) => (
                    <li key={chapter.title}>
                        <Button asChild variant="ghost" className="w-full justify-between h-auto py-4 group">
                            <Link href={chapter.url}>
                                <span className="text-lg">{chapter.title}</span>
                                <ArrowRight className="h-5 w-5 transition-transform group-hover:translate-x-1" />
                            </Link>
                        </Button>
                    </li>
                ))}
            </ul>
        </div>
      </div>
    </div>
  );
}
