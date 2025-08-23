import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { ShieldCheck, Target, BookOpenCheck, ListCollapse, ArrowRight, Search, Users, Code, PenTool } from "lucide-react";
import Link from "next/link";

export default async function Home() {
  
  return (
    <div className="flex flex-col min-h-screen">
      <main className="flex-1">
        {/* Hero Section */}
        <section className="w-full py-20 md:py-32 lg:py-40 bg-background relative overflow-hidden">
          <div className="absolute inset-0 w-full h-full bg-[radial-gradient(ellipse_80%_80%_at_50%_-20%,hsl(var(--primary)/0.3),rgba(255,255,255,0))]"></div>
          <div className="container mx-auto px-4 md:px-6 text-center relative z-10">
            <div className="mx-auto max-w-3xl space-y-4">
              <div className="inline-block rounded-lg bg-secondary px-3 py-1 text-sm text-secondary-foreground animate-text-flicker">Your Partner in Cyber Defense</div>
              <h1 className="text-4xl font-bold tracking-tighter sm:text-5xl md:text-6xl lg:text-7xl text-primary-foreground [text-shadow:0_0_10px_hsl(var(--primary)/0.7)]">
                SutraByte
              </h1>
              <p className="text-lg text-muted-foreground md:text-xl">
                Empowering individuals and organizations with cutting-edge cybersecurity resources, training, and skill assessments.
              </p>
              <div className="flex flex-col gap-2 min-[400px]:flex-row justify-center">
                <Button asChild size="lg" variant="secondary">
                  <Link href="/resources">
                    Explore Resources
                  </Link>
                </Button>
              </div>
            </div>
          </div>
        </section>

        {/* Our Services Section */}
        <section className="w-full py-12 md:py-24 lg:py-32">
          <div className="container mx-auto px-4 md:px-6">
            <div className="flex flex-col items-center justify-center space-y-4 text-center mb-12">
              <div className="inline-block rounded-lg bg-secondary px-3 py-1 text-sm text-secondary-foreground">Our Services</div>
              <h2 className="text-3xl font-bold tracking-tighter sm:text-5xl">Our Services</h2>
              <p className="max-w-[900px] text-muted-foreground md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed">
                Empowering Businesses with Security, Skills & Digital Solutions
              </p>
            </div>
            <div className="mx-auto grid max-w-6xl items-start gap-6 sm:grid-cols-2 md:gap-8 lg:grid-cols-4">
              <Card className="bg-card/50 transition-all transform hover:-translate-y-1 hover:shadow-glow hover:border-primary">
                <CardHeader className="flex flex-col items-center gap-4 text-center">
                  <div className="rounded-md bg-primary p-3 text-primary-foreground">
                    <Search className="h-6 w-6" />
                  </div>
                  <CardTitle>Cybersecurity Testing (VAPT)</CardTitle>
                </CardHeader>
                <CardContent className="text-center">
                  <p className="text-muted-foreground">Find and fix vulnerabilities before attackers do.</p>
                </CardContent>
              </Card>
              <Card className="bg-card/50 transition-all transform hover:-translate-y-1 hover:shadow-glow hover:border-primary">
                <CardHeader className="flex flex-col items-center gap-4 text-center">
                  <div className="rounded-md bg-primary p-3 text-primary-foreground">
                    <Users className="h-6 w-6" />
                  </div>
                  <CardTitle>Awareness Training</CardTitle>
                </CardHeader>
                <CardContent className="text-center">
                  <p className="text-muted-foreground">Make your team your first line of defense.</p>
                </CardContent>
              </Card>
              <Card className="bg-card/50 transition-all transform hover:-translate-y-1 hover:shadow-glow hover:border-primary">
                <CardHeader className="flex flex-col items-center gap-4 text-center">
                  <div className="rounded-md bg-primary p-3 text-primary-foreground">
                    <Code className="h-6 w-6" />
                  </div>
                  <CardTitle>Web Development & Security</CardTitle>
                </CardHeader>
                <CardContent className="text-center">
                  <p className="text-muted-foreground">Build secure, responsive, and modern websites.</p>
                </CardContent>
              </Card>
              <Card className="bg-card/50 transition-all transform hover:-translate-y-1 hover:shadow-glow hover:border-primary">
                <CardHeader className="flex flex-col items-center gap-4 text-center">
                  <div className="rounded-md bg-primary p-3 text-primary-foreground">
                    <PenTool className="h-6 w-6" />
                  </div>
                  <CardTitle>Content & Technical Writing</CardTitle>
                </CardHeader>
                <CardContent className="text-center">
                  <p className="text-muted-foreground">Educate and engage with high-quality content.</p>
                </CardContent>
              </Card>
            </div>
            <div className="flex justify-center mt-12">
              <Button asChild size="lg" className="group">
                <Link href="/services">
                  See All Services <ArrowRight className="ml-2 h-5 w-5 transition-transform group-hover:translate-x-1" />
                </Link>
              </Button>
            </div>
          </div>
        </section>

        {/* Features Section */}
        <section id="features" className="w-full py-12 md:py-24 lg:py-32">
          <div className="container mx-auto px-4 md:px-6">
            <div className="flex flex-col items-center justify-center space-y-4 text-center mb-12">
              <div className="inline-block rounded-lg bg-secondary px-3 py-1 text-sm text-secondary-foreground">Key Features</div>
              <h2 className="text-3xl font-bold tracking-tighter sm:text-5xl">Level Up Your Cyber Skills</h2>
              <p className="max-w-[900px] text-muted-foreground md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed">
                Our platform provides everything you need to stay ahead of the curve in the fast-paced world of cybersecurity.
              </p>
            </div>
            <div className="mx-auto grid max-w-5xl items-start gap-8 sm:grid-cols-2 md:gap-12 lg:grid-cols-3">
              
              <Card className="bg-card/50 transition-all transform hover:-translate-y-1 hover:shadow-glow hover:border-primary">
                <CardHeader className="flex flex-row items-center gap-4">
                  <div className="rounded-md bg-primary p-3 text-primary-foreground">
                    <BookOpenCheck className="h-6 w-6" />
                  </div>
                  <CardTitle>Learning Series</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">Enroll in our 45-day structured program to systematically enhance your cybersecurity expertise.</p>
                </CardContent>
              </Card>
              <Card className="bg-card/50 transition-all transform hover:-translate-y-1 hover:shadow-glow hover:border-primary">
                <CardHeader className="flex flex-row items-center gap-4">
                  <div className="rounded-md bg-primary p-3 text-primary-foreground">
                    <ListCollapse className="h-6 w-6" />
                  </div>
                  <CardTitle>Resource Directory</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">Access a curated library of articles, tools, and guides, intelligently tagged for easy discovery.</p>
                </CardContent>
              </Card>
            </div>
          </div>
        </section>
        
        {/* CTA Section */}
        <section className="w-full py-12 md:py-24 lg:py-32">
          <div className="container mx-auto grid items-center justify-center gap-4 px-4 text-center md:px-6">
            <div className="space-y-3">
              <h2 className="text-3xl font-bold tracking-tighter md:text-4xl/tight">Ready to fortify your defenses?</h2>
              <p className="mx-auto max-w-[600px] text-muted-foreground md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed">
                Explore our resources and start your journey towards cybersecurity mastery today.
              </p>
            </div>
            <div className="mx-auto w-full max-w-sm space-y-2">
               <Button asChild size="lg" className="w-full group">
                  <Link href="/resources">
                    Explore Resources <ArrowRight className="ml-2 h-5 w-5 transition-transform group-hover:translate-x-1" />
                  </Link>
                </Button>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
}
