
import { notFound } from 'next/navigation';
import { roadmaps } from '@/lib/roadmaps-data';
import { Button } from '@/components/ui/button';
import Link from 'next/link';
import { ArrowLeft } from 'lucide-react';

type PdfViewerPageProps = {
  params: {
    slug: string;
  };
};

export default function PdfViewerPage({ params }: PdfViewerPageProps) {
  const roadmap = roadmaps.find((r) => r.url === params.slug && r.type === 'pdf');

  if (!roadmap) {
    notFound();
  }

  // We construct the path to the PDF file in the public directory
  const pdfUrl = `/roadmaps/${roadmap.url}.pdf`;

  return (
    <div className="container mx-auto px-4 md:px-6 py-8 flex flex-col" style={{ height: 'calc(100vh - 8rem)' }}>
        <div className="mb-8">
            <Button asChild variant="outline" className="group">
                <Link href="/roadmaps">
                    <ArrowLeft className="mr-2 h-5 w-5 transition-transform group-hover:-translate-x-1" />
                    Back to Roadmaps
                </Link>
            </Button>
        </div>
        <div className="text-center mb-8">
            <h1 className="text-3xl font-bold tracking-tighter sm:text-4xl">{roadmap.title}</h1>
        </div>
        <div className="flex-grow">
            <iframe
            src={pdfUrl}
            className="w-full h-full border-0 rounded-lg shadow-lg"
            title={roadmap.title}
            >
            This browser does not support PDFs. Please download the PDF to view it.
            </iframe>
        </div>
    </div>
  );
}

export async function generateStaticParams() {
    return roadmaps
      .filter(roadmap => roadmap.type === 'pdf')
      .map((roadmap) => ({
        slug: roadmap.url,
      }));
}
