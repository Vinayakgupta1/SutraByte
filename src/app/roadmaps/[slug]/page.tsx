
import { promises as fs } from 'fs';
import path from 'path';
import { notFound } from 'next/navigation';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { roadmaps } from '@/lib/roadmaps-data';
import { Badge } from '@/components/ui/badge';
import Link from 'next/link';
import { Button } from '@/components/ui/button';
import { ArrowLeft } from 'lucide-react';

type RoadmapPageProps = {
  params: {
    slug: string;
  };
};

async function getRoadmapContent(slug: string) {
  const roadmap = roadmaps.find((r) => r.url === slug);
  if (!roadmap) {
    return null;
  }

  const filePath = path.join(process.cwd(), 'public', 'roadmaps', `${slug}.md`);
  
  try {
    const content = await fs.readFile(filePath, 'utf-8');
    return {
      content,
      roadmap,
    };
  } catch (error) {
    console.error(`Error reading markdown file for roadmap: ${slug}`, error);
    return null;
  }
}

export async function generateStaticParams() {
  return roadmaps.map((roadmap) => ({
    slug: roadmap.url,
  }));
}

export default async function RoadmapPage({ params }: RoadmapPageProps) {
  const data = await getRoadmapContent(params.slug);

  if (!data) {
    notFound();
  }

  const { content, roadmap } = data;

  return (
    <div className="container mx-auto px-4 md:px-6 py-12">
      <div className="max-w-4xl mx-auto">
        <div className="mb-8">
            <Button asChild variant="outline" className="group">
                <Link href="/roadmaps">
                    <ArrowLeft className="mr-2 h-5 w-5 transition-transform group-hover:-translate-x-1" />
                    Back to Roadmaps
                </Link>
            </Button>
        </div>
        <div className="mb-12 text-center">
          <h1 className="text-4xl font-bold tracking-tighter sm:text-5xl">{roadmap.title}</h1>
           <div className="flex justify-center flex-wrap gap-2 mt-4">
            {roadmap.tags.map(tag => (
              <Badge key={tag} variant="secondary">{tag}</Badge>
            ))}
          </div>
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
