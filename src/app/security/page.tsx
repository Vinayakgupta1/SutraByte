import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { ShieldCheck, Lock, DatabaseZap } from "lucide-react";

export default function SecurityPage() {
  return (
    <div className="container mx-auto px-4 md:px-6 py-12 md:py-24">
      <div className="text-center space-y-4 mb-12">
        <h1 className="text-4xl font-bold tracking-tighter sm:text-5xl md:text-6xl">Our Commitment to Security</h1>
        <p className="max-w-[700px] mx-auto text-muted-foreground md:text-xl">
          At SutraByte, security is not just a feature; it's the foundation of our platform.
        </p>
      </div>

      <div className="max-w-4xl mx-auto grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        <Card>
          <CardHeader className="flex flex-row items-center gap-4">
            <div className="p-3 bg-primary rounded-md text-primary-foreground">
                <ShieldCheck className="h-6 w-6" />
            </div>
            <CardTitle>Platform Security</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-muted-foreground">We follow industry best practices, including regular security audits and penetration testing, to ensure our platform is secure against threats.</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="flex flex-row items-center gap-4">
            <div className="p-3 bg-primary rounded-md text-primary-foreground">
                <Lock className="h-6 w-6" />
            </div>
            <CardTitle>Data Encryption</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-muted-foreground">All data, both at rest and in transit, is encrypted using strong, industry-standard cryptographic protocols to protect your information.</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="flex flex-row items-center gap-4">
            <div className="p-3 bg-primary rounded-md text-primary-foreground">
                <DatabaseZap className="h-6 w-6" />
            </div>
            <CardTitle>Secure Authentication</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-muted-foreground">We enforce secure password policies and offer multi-factor authentication options to protect your account from unauthorized access.</p>
          </CardContent>
        </Card>
      </div>

      <div className="max-w-4xl mx-auto mt-16">
        <h2 className="text-3xl font-bold text-center mb-8">Compliance & Certifications</h2>
        <p className="text-center text-muted-foreground mb-8">
            We are continuously working to meet and exceed industry security standards. While we are in the process of obtaining formal certifications, our practices are aligned with frameworks like SOC 2 and ISO 27001.
        </p>
        <div className="flex justify-center items-center gap-8">
            <div className="text-center text-muted-foreground">
                <p className="font-bold text-lg text-foreground">SOC 2</p>
                <p>In Progress</p>
            </div>
             <div className="text-center text-muted-foreground">
                <p className="font-bold text-lg text-foreground">ISO 27001</p>
                <p>In Progress</p>
            </div>
             <div className="text-center text-muted-foreground">
                <p className="font-bold text-lg text-foreground">GDPR</p>
                <p>Compliant</p>
            </div>
        </div>
      </div>
    </div>
  );
}
