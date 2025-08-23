import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';
import { Toaster } from "@/components/ui/toaster"
import { Header } from '@/components/common/Header';
import { Footer } from '@/components/common/Footer';
import { ThemeProvider } from '@/components/common/ThemeProvider';

const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-inter',
});

export const metadata: Metadata = {
  metadataBase: new URL('https://sutrabyte.vercel.app'), // Updated deployment URL
  title: 'SutraByte - Learn Cybersecurity Skills',
  description: 'Enhance your cybersecurity knowledge and practices with SutraByte. Join our 45-day learning series covering everything from basics to advanced security concepts.',
  keywords: 'cybersecurity, ethical hacking, network security, penetration testing, information security, cyber defense',
  authors: [{ name: 'SutraByte Team' }],
  openGraph: {
    type: 'website',
    locale: 'en_US',
    url: 'https://sutrabyte.com',
    siteName: 'SutraByte',
    title: 'SutraByte - Learn Cybersecurity Skills',
    description: 'Enhance your cybersecurity knowledge and practices with SutraByte. Join our 45-day learning series.',
    images: [
      {
        url: '/og-image.png', // Add your Open Graph image
        width: 1200,
        height: 630,
        alt: 'SutraByte Cybersecurity Learning Platform',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'SutraByte - Learn Cybersecurity Skills',
    description: 'Enhance your cybersecurity knowledge and practices with SutraByte.',
    images: ['/og-image.png'], // Add your Twitter card image
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-video-preview': -1,
      'max-image-preview': 'large',
      'max-snippet': -1,
    },
  },
  verification: {
    google: 'sj0yOPAf8-SI2cN28NunsTEQEOcGsI9JwErpSRqOyaU', // Updated verification code
  },
  alternates: {
    canonical: 'https://sutrabyte.vercel.app', // Updated canonical URL
  },
};

export default async function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={inter.variable} suppressHydrationWarning>
      <body className="font-body antialiased">
        <ThemeProvider
          attribute="class"
          defaultTheme="system"
          enableSystem
          disableTransitionOnChange
        >
          <div className="relative flex min-h-screen flex-col">
            <Header />
            <main className="flex-1 container max-w-[1400px] mx-auto">
              {children}
            </main>
            <Footer />
          </div>
          <Toaster />
        </ThemeProvider>
      </body>
    </html>
  );
}
