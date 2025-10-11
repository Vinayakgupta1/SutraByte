import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Linkedin, User, ArrowUpRight, Youtube, Instagram, Link as LinkIcon } from "lucide-react";
import Link from "next/link";

const socialLinks = [
    {
        name: 'SutraByte on LinkedIn',
        href: 'https://www.linkedin.com/company/sutrabyte',
        icon: <Linkedin className="h-6 w-6 text-primary" />,
    },
    {
        name: 'SutraByte on YouTube',
        href: 'https://www.youtube.com/@sutrabyte1',
        icon: <Youtube className="h-6 w-6 text-primary" />,
    },
    {
        name: 'SutraByte on Instagram',
        href: 'https://www.instagram.com/sutrabyte1',
        icon: <Instagram className="h-6 w-6 text-primary" />,
    },
    {
        name: 'Vinayak (Founder) - LinkedIn',
        href: 'https://www.linkedin.com/in/vinayak15/',
        icon: <Linkedin className="h-6 w-6 text-primary" />,
    },
    {
        name: 'Vinayak (Founder) - Portfolio',
        href: 'https://vinayakgupta15.github.io/Vinayak-Portfolio/',
        icon: <User className="h-6 w-6 text-primary" />,
    },
    {
        name: 'Linktree',
        href: 'https://linktr.ee/vinayak1544',
        icon: <LinkIcon className="h-6 w-6 text-primary" />,
    },
    {
        name: 'Anushika (Co-Founder) - LinkedIn',
        href: 'https://www.linkedin.com/in/anushika-dutta-a04959313/',
        icon: <User className="h-6 w-6 text-primary" />,
    },
];

export default function ContactPage() {
  return (
    <div className="container mx-auto px-4 md:px-6 py-12 md:py-24">
      <div className="text-center space-y-4 mb-12">
        <h1 className="text-4xl font-bold tracking-tighter sm:text-5xl md:text-6xl">Connect With Us</h1>
        <p className="max-w-[700px] mx-auto text-muted-foreground md:text-xl">
          Follow us and our team on social media to stay updated with our latest activities and insights.
        </p>
      </div>

      <div className="max-w-2xl mx-auto">
        <Card>
            <CardHeader>
                <CardTitle>Our Links</CardTitle>
                <CardDescription>Find us on these platforms.</CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
                {socialLinks.map((link) => (
                    <Button key={link.href} asChild variant="outline" className="w-full justify-start text-left h-auto py-3">
                        <Link href={link.href} target="_blank" rel="noopener noreferrer" className="flex items-center w-full gap-4">
                           <div className="shrink-0">{link.icon}</div>
                           <div className="flex-grow min-w-0">
                               <span className="break-words">{link.name}</span>
                           </div>
                           <ArrowUpRight className="h-5 w-5 text-muted-foreground shrink-0 ml-auto" />
                        </Link>
                    </Button>
                ))}
            </CardContent>
        </Card>
      </div>
    </div>
  );
}
