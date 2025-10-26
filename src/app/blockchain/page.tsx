import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { ArrowRight, Gift } from "lucide-react";
import Link from "next/link";

export default function BlockchainPage() {
  const nftFormUrl = "https://forms.gle/Ps3DmxpxUEKeEBw36";

  return (
    <div className="container mx-auto px-4 md:px-6 py-12 md:py-24">
      <div className="flex flex-col items-center justify-center text-center space-y-8">
        <div className="space-y-4">
            <h1 className="text-4xl font-bold tracking-tighter sm:text-5xl md:text-6xl">SutraByte NFTs</h1>
            <p className="max-w-[700px] mx-auto text-muted-foreground md:text-xl">
            A special collection of NFTs for the SutraByte family to celebrate our community.
            </p>
        </div>

        <Card className="max-w-lg w-full transition-all hover:shadow-glow hover:border-primary">
            <CardHeader className="items-center text-center">
                <Gift className="h-16 w-16 text-primary mb-4" />
                <CardTitle className="text-2xl">Claim Your Exclusive NFT</CardTitle>
                <CardDescription>
                    As a valued member of our community, you are invited to claim a unique SutraByte NFT. Fill out the form to get yours!
                </CardDescription>
            </CardHeader>
            <CardContent>
                <Button asChild size="lg" className="w-full group">
                    <Link href={nftFormUrl} target="_blank" rel="noopener noreferrer">
                        Claim Your NFT <ArrowRight className="ml-2 h-5 w-5 transition-transform group-hover:translate-x-1" />
                    </Link>
                </Button>
            </CardContent>
        </Card>
      </div>
    </div>
  );
}
