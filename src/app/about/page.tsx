import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { SutraByteLogo } from "@/components/icons/SutraByteLogo";
import { Button } from "@/components/ui/button";
import Link from "next/link";
import { ArrowRight } from 'lucide-react';

export default function AboutPage() {
  return (
    <div className="container mx-auto px-4 md:px-6 py-12 md:py-24">
      <div className="text-center space-y-4 mb-12">
        <SutraByteLogo className="h-24 w-24 mx-auto" />
        <h1 className="text-4xl font-bold tracking-tighter sm:text-5xl md:text-6xl">About SutraByte</h1>
        <p className="text-xl text-primary font-semibold">Empowering the Next Generation of Cyber Defenders</p>
      </div>

      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        <Card className="transition-all hover:shadow-glow hover:border-primary">
          <CardHeader>
            <CardTitle>Our Mission</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-muted-foreground">
              To make cybersecurity education <strong className="text-foreground">accessible, ethical, and actionable</strong> for everyone—regardless of background or prior experience. We aim to build a safer digital world by equipping individuals with <strong className="text-foreground">structured, step-by-step learning paths</strong>, practical resources, and <strong className="text-foreground">real-world insights</strong> into ethical hacking and defense.
            </p>
          </CardContent>
        </Card>

        <Card className="transition-all hover:shadow-glow hover:border-primary">
          <CardHeader>
            <CardTitle>Our Vision</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-muted-foreground">
              To evolve as a leading global platform where <strong className="text-foreground">timeless wisdom meets modern cybersecurity practices</strong>. SutraByte envisions a vibrant community of <strong className="text-foreground">ethical hackers, cyber defenders, and security innovators</strong> who actively shape the future of digital safety.
            </p>
          </CardContent>
        </Card>

        <Card className="transition-all hover:shadow-glow hover:border-primary lg:col-span-1 md:col-span-2">
          <CardHeader>
            <CardTitle>Our Values</CardTitle>
          </CardHeader>
          <CardContent>
            <ul className="space-y-2 text-muted-foreground list-disc list-inside">
              <li><strong className="text-foreground">Accessibility:</strong> Learning should be free, open, and inclusive for everyone—no matter their background.</li>
              <li><strong className="text-foreground">Ethics:</strong> We promote responsible, legal, and purposeful use of cybersecurity skills to protect and uplift.</li>
              <li><strong className="text-foreground">Innovation:</strong> We blend ancient principles with cutting-edge digital practices to create practical knowledge.</li>
              <li><strong className="text-foreground">Community:</strong> We grow together—learning, supporting, and mentoring each other as a global cyber tribe.</li>
            </ul>
          </CardContent>
        </Card>

        <Card className="transition-all hover:shadow-glow hover:border-primary md:col-span-1 lg:col-span-2">
          <CardHeader>
            <CardTitle>Why SutraByte?</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-muted-foreground mb-2">
              <strong className="text-foreground">Sutra (सूत्र):</strong> A Sanskrit word meaning "thread," "guideline," or "formula"—symbolizing timeless wisdom and structured learning.
            </p>
            <p className="text-muted-foreground">
              <strong className="text-foreground">Byte:</strong> The building block of digital information in computing.
            </p>
            <p className="text-muted-foreground mt-4 italic">
              SutraByte weaves these two worlds together—<strong className="text-foreground">fusing ancient wisdom and modern digital intelligence</strong> to build a safer, smarter cyber world.
            </p>
          </CardContent>
        </Card>

        <Card className="transition-all hover:shadow-glow hover:border-primary md:col-span-1 lg:col-span-1">
          <CardHeader>
            <CardTitle>Meet the Founder</CardTitle>
            <p className="text-primary">Vinayak (CyberGupta)</p>
            <p className="text-sm text-muted-foreground">Penetration Tester, Ethical Hacker, and Cybersecurity Enthusiast</p>
          </CardHeader>
          <CardContent>
            <blockquote className="border-l-4 border-accent pl-4 italic text-muted-foreground">
              "I started SutraByte to break down barriers in cybersecurity education. My mission is to inspire, guide, and empower the next generation of cyber defenders—making security a habit, not just a skill."
            </blockquote>
          </CardContent>
        </Card>
      </div>

       <div className="mt-16 text-center">
        <h3 className="text-2xl font-bold tracking-tighter mb-4">Have Questions?</h3>
         <p className="max-w-[600px] mx-auto text-muted-foreground md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed mb-6">
            We'd love to hear from you. Whether you have a question about our resources, feedback, or anything else, our team is ready to answer all your questions.
         </p>
         <Button asChild size="lg" className="group">
            <Link href="/contact">
              Contact Us <ArrowRight className="ml-2 h-5 w-5 transition-transform group-hover:translate-x-1" />
            </Link>
         </Button>
      </div>

    </div>
  );
}
