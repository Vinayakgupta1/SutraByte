
import { promises as fs } from 'fs';
import path from 'path';
import { notFound } from 'next/navigation';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { books } from '@/lib/books-data';
import { Badge } from '@/components/ui/badge';
import Link from 'next/link';
import { Button } from '@/components/ui/button';
import { ArrowLeft } from 'lucide-react';

type ChapterPageProps = {
  params: {
    slug: string;
    chapter: string;
  } | Promise<{
    slug: string;
    chapter: string;
  }>;
};

export async function generateStaticParams() {
  const paths: { slug: string; chapter: string }[] = [];

  const multiChapterBooks = books.filter((book) => book.type === 'multichapter');

  multiChapterBooks.forEach((book) => {
    if (book.summary) {
      paths.push({ slug: book.url, chapter: 'summary' });
    }
    if (book.chapters) {
      for (let i = 1; i <= book.chapters; i++) {
        paths.push({ slug: book.url, chapter: `chapter-${i}` });
      }
    }
  });

  return paths;
}

async function getChapterContent(slug: string, chapterSlug: string) {
  const book = books.find((b) => b.type === 'multichapter' && b.url === slug);
  if (!book) {
    return null;
  }

  const filePath = path.join(process.cwd(), 'public', 'books', slug, `${chapterSlug}.md`);
  
  try {
    const content = await fs.readFile(filePath, 'utf-8');
    
    let chapterTitle = '';
    if (chapterSlug === 'summary') {
        chapterTitle = 'Summary Chapter';
    } else if (chapterSlug.startsWith('chapter-')) {
        chapterTitle = `Project Chapter ${chapterSlug.split('-')[1]}`;
    }

    return {
      content,
      book,
      chapterTitle,
    };
  } catch (error) {
    console.error(`Error reading markdown file for chapter: ${slug}/${chapterSlug}`, error);
    return null;
  }
}


export default async function ChapterPage({ params }: ChapterPageProps) {
  const resolvedParams = await params;
  const data = await getChapterContent(resolvedParams.slug, resolvedParams.chapter);

  if (!data) {
    notFound();
  }

  const { content, book, chapterTitle } = data;

  return (
    <div className="container mx-auto px-4 md:px-6 py-12">
      <div className="max-w-4xl mx-auto">
        <div className="mb-8">
            <Button asChild variant="outline" className="group">
                <Link href={`/books/${book.url}`}>
                    <ArrowLeft className="mr-2 h-5 w-5 transition-transform group-hover:-translate-x-1" />
                    Back to Table of Contents
                </Link>
            </Button>
        </div>
        <div className="mb-12 text-center">
          <h1 className="text-4xl font-bold tracking-tighter sm:text-5xl">{book.title}</h1>
          <h2 className="text-2xl mt-2 text-primary">{chapterTitle}</h2>
        </div>
        
        <article className="prose prose-invert max-w-none markdown-content">
          <ReactMarkdown remarkPlugins={[remarkGfm]}>
            {content}
          </ReactMarkdown>
        </article>
      </div>
    </div>
  );
}
