import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import "katex/dist/katex.min.css";
import { getCategories } from "@/lib/mdx";
import { Sidebar } from "@/components/Sidebar";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Flashcards de Algoritmos",
  description:
    "Revisa os teus algoritmos de LeetCode com flashcards interativos",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const categories = getCategories();

  return (
    <html lang="pt">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        <div className="flex min-h-screen">
          <Sidebar categories={categories} />
          <main className="flex-1 overflow-y-auto px-4 py-8 md:px-8 lg:px-12 pt-16 md:pt-8">
            {children}
          </main>
        </div>
      </body>
    </html>
  );
}
