'use client';

import Link from 'next/link';
import { Button } from '@/components/ui/button';
import { DialogTitle } from "@/components/ui/dialog";
import { Sheet, SheetContent, SheetTrigger } from '@/components/ui/sheet';
import { Menu } from 'lucide-react';
import { NAV_LINKS } from '@/lib/constants';
import { usePathname } from 'next/navigation';
import { cn } from '@/lib/utils';
import { SutraByteLogo } from '@/components/icons/SutraByteLogo';
import { ThemeToggle } from './ThemeToggle';

export function Header({ children }: { children?: React.ReactNode }) {
  const pathname = usePathname();

  return (
    <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container mx-auto max-w-5xl px-4 md:px-6 py-6">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-8">
            <Link href="/" className="flex items-center space-x-3">
              <SutraByteLogo className="h-10 w-10" />
              <span className="text-xl font-bold">SutraByte</span>
            </Link>
            
            <nav className="hidden md:flex items-center space-x-6">
              {NAV_LINKS.map((link) => (
                <Link
                  key={link.href}
                  href={link.href}
                  className={cn(
                    'transition-colors hover:text-primary px-4 py-3 rounded-md text-base font-medium',
                    pathname === link.href ? 'text-primary' : 'text-muted-foreground'
                  )}
                >
                  {link.label}
                </Link>
              ))}
            </nav>
          </div>

          <div className="flex items-center space-x-6">
            <ThemeToggle />
            {children}
            <Sheet>
              <SheetTrigger asChild>
                <Button 
                  variant="ghost" 
                  className="md:hidden p-3"
                >
                  <Menu className="h-6 w-6" />
                  <span className="sr-only">Toggle Menu</span>
                </Button>
              </SheetTrigger>
              <SheetContent side="left" className="pr-0">
                <DialogTitle className="sr-only">Navigation Menu</DialogTitle>
                <Link href="/" className="flex items-center space-x-2 p-6">
                  <SutraByteLogo className="h-10 w-10" />
                  <span className="text-xl font-bold">SutraByte</span>
                </Link>
                <div key={pathname} className="my-4 h-[calc(100vh-8rem)] pb-10 pl-6">
                  <div className="flex flex-col space-y-4">
                    {NAV_LINKS.map((link) => (
                      <Link
                        key={link.href}
                        href={link.href}
                        className={cn(
                          'transition-colors hover:text-primary text-lg p-2',
                          pathname === link.href ? 'text-primary' : 'text-muted-foreground'
                        )}
                      >
                        {link.label}
                      </Link>
                    ))}
                  </div>
                </div>
              </SheetContent>
            </Sheet>
          </div>
        </div>
      </div>
    </header>
  );
}
