import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';
import { Toaster } from "@/components/ui/toaster"
import { Header } from '@/components/common/Header';
import { Footer } from '@/components/common/Footer';
import { ThemeProvider } from '@/components/common/ThemeProvider';
import { Analytics } from "@vercel/analytics/react"

const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-inter',
});

export const metadata: Metadata = {
  title: 'SutraByte',
  description: 'Enhance your cybersecurity knowledge and practices with SutraByte.',
};

export default async function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  
  return (
    <html lang="en" className={inter.variable} suppressHydrationWarning>
      <head>
        <meta name="google-site-verification" content="sj0yOPAf8-SI2cN28NunsTEQEOcGsI9JwErpSRqOyaU" />
      </head>
      <body className="font-body antialiased">
            <ThemeProvider
            attribute="class"
            defaultTheme="system"
            enableSystem
            disableTransitionOnChange
            >
            <div className="relative flex min-h-screen flex-col">
                <Header />
                <main className="flex-1">
                {children}
                </main>
                <Footer />
            </div>
            <Toaster />
            </ThemeProvider>
            <Analytics />
      </body>
    </html>
  );
}