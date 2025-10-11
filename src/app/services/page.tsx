import { Card, CardContent, CardHeader, CardTitle, CardFooter } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import Link from "next/link";
import { ArrowRight } from "lucide-react";

const services = [
  { 
    title: "Cybersecurity Testing (VAPT)", 
    emoji: "🔍", 
    description: "In-depth vulnerability assessment and penetration testing to identify and remediate security weaknesses in your applications and networks.",
  },
  { 
    title: "Awareness Training", 
    emoji: "🎯", 
    description: "Customized training programs to educate your employees on recognizing and responding to cyber threats like phishing and social engineering.",
  },
  { 
    title: "Web Development & Security", 
    emoji: "💻", 
    description: "Building secure, high-performance, and responsive websites from the ground up with a security-first approach.",
  },
  { 
    title: "Content & Technical Writing", 
    emoji: "✍️", 
    description: "Creating high-quality, engaging, and technically accurate content, including blog posts, whitepapers, and documentation.",
  },
  { 
    title: "Security Audits & Compliance", 
    emoji: "🛡️", 
    description: "Assessing your security posture against industry standards and regulations to ensure you meet compliance requirements.",
  },
   { 
    title: "Smart Contract in Blockchain", 
    emoji: "⛓️", 
    description: "Auditing and developing secure smart contracts to ensure the integrity and safety of your blockchain applications.",
  },
];

export default function ServicesPage() {
  return (
    <div className="container mx-auto px-4 md:px-6 py-12 md:py-24">
      <div className="text-center space-y-4 mb-12">
        <h1 className="text-4xl font-bold tracking-tighter sm:text-5xl md:text-6xl">Our Services</h1>
        <p className="max-w-[700px] mx-auto text-muted-foreground md:text-xl">
          A comprehensive suite of solutions to protect and enhance your digital presence.
        </p>
      </div>

      <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-8">
        {services.map((service) => (
          <Card key={service.title} className="flex flex-col items-center text-center p-8 transition-all hover:shadow-glow hover:border-primary">
             <div className="text-5xl md:text-6xl mb-4">{service.emoji}</div>
            <CardHeader>
              <CardTitle>{service.title}</CardTitle>
            </CardHeader>
            <CardContent className="flex-grow">
              <p className="text-muted-foreground">{service.description}</p>
            </CardContent>
          </Card>
        ))}
      </div>

      <div className="mt-16 text-center">
        <h3 className="text-2xl font-bold tracking-tighter mb-4">Interested in our services?</h3>
         <p className="max-w-[600px] mx-auto text-muted-foreground md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed mb-6">
            Ready to get started? Fill out our service request form and we'll get in touch with you.
         </p>
         <Button asChild size="lg" className="group">
            <Link href="https://docs.google.com/forms/d/e/1FAIpQLSfs4xmkkmz1Q2sm02RqfWF4vXZBSZhsQCXlQG7tSFTWr7Sc0Q/viewform?usp=header" target="_blank" rel="noopener noreferrer">
              Request Service <ArrowRight className="ml-2 h-5 w-5 transition-transform group-hover:translate-x-1" />
            </Link>
         </Button>
      </div>

    </div>
  );
}
