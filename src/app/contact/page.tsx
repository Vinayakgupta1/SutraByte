import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Linkedin, User, ArrowUpRight } from "lucide-react";
import Link from "next/link";

const socialLinks = [
    {
        name: 'SutraByte on LinkedIn',
        href: 'https://www.linkedin.com/company/sutrabyte',
        icon: <Linkedin className="h-6 w-6 text-primary" />,
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
        name: 'Anushika (Co-Founder) - LinkedIn',
        href: 'https://www.linkedin.com/in/anushika-dutta-a04959313/',
        icon: <User className="h-6 w-6 text-primary" />,
    },
    {
        name: 'Anushika (Co-Founder) - Portfolio',
        href: 'https://anushika006.github.io/Anushika-Portfolio/',
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
                    <Button key={link.href} asChild variant="outline" className="w-full justify-start gap-4 text-left h-auto py-3">
                        <Link href={link.href} target="_blank" rel="noopener noreferrer">
                           {link.icon}
                           <span className="flex-grow">{link.name}</span>
                           <ArrowUpRight className="h-5 w-5 text-muted-foreground" />
                        </Link>
                    </Button>
                ))}
            </CardContent>
        </Card>
      </div>
    </div>
  );
}
