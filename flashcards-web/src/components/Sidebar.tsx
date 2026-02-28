"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { Menu } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet";
import type { CategoryMeta } from "@/lib/mdx";
import { useState } from "react";

interface SidebarProps {
  categories: CategoryMeta[];
}

function NavLinks({
  categories,
  onClick,
}: {
  categories: CategoryMeta[];
  onClick?: () => void;
}) {
  const pathname = usePathname();

  return (
    <nav className="flex flex-col gap-1">
      <Link
        href="/"
        onClick={onClick}
        className={`rounded-md px-3 py-2 text-sm font-medium transition-colors hover:bg-accent ${
          pathname === "/" ? "bg-accent text-accent-foreground" : ""
        }`}
      >
        Inicio
      </Link>
      {categories.map((cat) => (
        <Link
          key={cat.slug}
          href={`/${cat.slug}`}
          onClick={onClick}
          className={`rounded-md px-3 py-2 text-sm transition-colors hover:bg-accent ${
            pathname === `/${cat.slug}`
              ? "bg-accent font-medium text-accent-foreground"
              : ""
          }`}
        >
          {cat.title}
        </Link>
      ))}
    </nav>
  );
}

export function Sidebar({ categories }: SidebarProps) {
  const [open, setOpen] = useState(false);

  return (
    <>
      {/* Desktop sidebar */}
      <aside className="hidden md:flex md:w-64 md:flex-col md:border-r md:bg-muted/40 md:p-4">
        <h2 className="mb-4 text-lg font-bold">Categorias</h2>
        <NavLinks categories={categories} />
      </aside>

      {/* Mobile hamburger */}
      <div className="fixed left-4 top-4 z-50 md:hidden">
        <Sheet open={open} onOpenChange={setOpen}>
          <SheetTrigger asChild>
            <Button variant="outline" size="icon">
              <Menu className="h-5 w-5" />
            </Button>
          </SheetTrigger>
          <SheetContent side="left" className="w-64 p-4">
            <h2 className="mb-4 text-lg font-bold">Categorias</h2>
            <NavLinks
              categories={categories}
              onClick={() => setOpen(false)}
            />
          </SheetContent>
        </Sheet>
      </div>
    </>
  );
}
