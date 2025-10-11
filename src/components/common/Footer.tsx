import Link from "next/link";
import { SutraByteLogo } from "@/components/icons/SutraByteLogo";

export function Footer() {
  return (
    <footer className="border-t border-border/40">
      <div className="container mx-auto flex flex-col items-center justify-between gap-4 py-8 md:flex-row md:py-6">
        <Link href="/" className="flex items-center space-x-2">
          <SutraByteLogo className="h-8 w-8" />
          <span className="text-lg font-bold">SutraByte</span>
        </Link>
        <p className="text-sm text-muted-foreground text-center md:text-left">
          © {new Date().getFullYear()} SutraByte. All Rights Reserved.
        </p>
      </div>
    </footer>
  );
}
