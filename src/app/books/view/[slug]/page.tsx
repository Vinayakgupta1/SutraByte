
import { notFound } from 'next/navigation';
import { books } from '@/lib/books-data';
import { Button } from '@/components/ui/button';
import Link from 'next/link';
import { ArrowLeft } from 'lucide-react';

type PdfViewerPageProps = {
  params: {
    slug: string;
  };
};

export default function PdfViewerPage({ params }: PdfViewerPageProps) {
  const book = books.find((b) => b.url === params.slug && b.type === 'pdf');

  if (!book) {
    notFound();
  }

  // We construct the path to the PDF file in the public directory
  const pdfUrl = `/books/${book.url}.pdf`;

  return (
    <div className="container mx-auto px-4 md:px-6 py-8 flex flex-col" style={{ height: 'calc(100vh - 8rem)' }}>
        <div className="mb-8">
            <Button asChild variant="outline" className="group">
                <Link href="/books">
                    <ArrowLeft className="mr-2 h-5 w-5 transition-transform group-hover:-translate-x-1" />
                    Back to Bookshelf
                </Link>
            </Button>
        </div>
        <div className="text-center mb-8">
            <h1 className="text-3xl font-bold tracking-tighter sm:text-4xl">{book.title}</h1>
        </div>
        <div className="flex-grow">
            <iframe
            src={pdfUrl}
            className="w-full h-full border-0 rounded-lg shadow-lg"
            title={book.title}
            >
            This browser does not support PDFs. Please download the PDF to view it.
            </iframe>
        </div>
    </div>
  );
}

export async function generateStaticParams() {
    return books
      .filter(book => book.type === 'pdf')
      .map((book) => ({
        slug: book.url,
      }));
}
