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
        <p className="max-w-[700px] mx-auto text-muted-foreground md:text-xl">
          Learn about our mission and the team behind SutraByte.
        </p>
      </div>

      <div className="grid md:grid-cols-3 gap-8 mb-12">
        {/* Why SutraByte Card */}
        <Card className="flex flex-col h-[320px] p-6 transition-all hover:shadow-glow hover:border-primary">
          <div>
            <CardTitle className="text-2xl mb-4">Why SutraByte?</CardTitle>
            <CardContent>
              <p className="text-muted-foreground">
                <strong className="text-foreground">Sutra (सूत्र):</strong> A Sanskrit word meaning "thread" or "guideline," symbolizing structured learning.
              </p>
              <p className="text-muted-foreground">
                <strong className="text-foreground">Byte:</strong> The building block of digital information.
              </p>
            </CardContent>
          </div>
        </Card>

        {/* Mission Card */}
        <Card className="flex flex-col h-[320px] p-6 transition-all hover:shadow-glow hover:border-primary">
          <div>
            <CardTitle className="text-2xl mb-4">Our Mission</CardTitle>
            <CardContent>
              <p className="text-muted-foreground">
                To make cybersecurity education <strong className="text-foreground">accessible, ethical, and actionable</strong> for everyone—equipping individuals with structured learning paths and practical resources.
              </p>
            </CardContent>
          </div>
        </Card>

        {/* Vision Card */}
        <Card className="flex flex-col h-[320px] p-6 transition-all hover:shadow-glow hover:border-primary">
          <div>
            <CardTitle className="text-2xl mb-4">Our Vision</CardTitle>
            <CardContent>
              <p className="text-muted-foreground">
                To evolve as a leading global platform where <strong className="text-foreground">timeless wisdom meets modern cybersecurity</strong>, building a community of ethical hackers and defenders.
              </p>
            </CardContent>
          </div>
        </Card>

        {/* Values Card */}
        <Card className="flex flex-col h-[320px] p-6 transition-all hover:shadow-glow hover:border-primary">
          <div>
            <CardTitle className="text-2xl mb-4">Our Values</CardTitle>
            <CardContent>
              <ul className="space-y-2 text-muted-foreground list-disc list-inside">
                <li><strong className="text-foreground">Accessibility:</strong> Free and inclusive learning</li>
                <li><strong className="text-foreground">Ethics:</strong> Responsible use of skills</li>
                <li><strong className="text-foreground">Innovation:</strong> Blending wisdom with practice</li>
                <li><strong className="text-foreground">Community:</strong> Growing together</li>
              </ul>
            </CardContent>
          </div>
        </Card>

        {/* Founder Card */}
        <Card className="flex flex-col h-[320px] p-6 transition-all hover:shadow-glow hover:border-primary">
          <div>
            <CardTitle className="text-2xl mb-4">Meet the Founder</CardTitle>
            <p className="text-primary">Vinayak (CyberGupta)</p>
            <p className="text-sm text-muted-foreground mb-4">Penetration Tester & Ethical Hacker</p>
            <CardContent>
              <blockquote className="border-l-4 border-accent pl-4 italic text-muted-foreground">
                "I started SutraByte to break down barriers in cybersecurity education. My mission is to inspire, guide, and empower the next generation of cyber defenders—making security a habit, not just a skill."
              </blockquote>
            </CardContent>
          </div>
        </Card>

        {/* Co-Founder Card */}
        <Card className="flex flex-col h-[320px] p-6 transition-all hover:shadow-glow hover:border-primary">
          <div>
            <CardTitle className="text-2xl mb-4">Meet the Co-Founder</CardTitle>
            <p className="text-primary">Anushika Dutta</p>
            <p className="text-sm text-muted-foreground mb-4">Cybersecurity Enthusiast</p>
            <CardContent>
              <blockquote className="border-l-4 border-accent pl-4 italic text-muted-foreground">
                "I helped start SutraByte because I believe learning cybersecurity should feel exciting, not intimidating. For me, it’s about sparking curiosity, encouraging creative problem‑solving, and helping people see that security isn’t just a skill — it’s a way of thinking that can change the digital world for the better."
              </blockquote>
            </CardContent>
          </div>
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
