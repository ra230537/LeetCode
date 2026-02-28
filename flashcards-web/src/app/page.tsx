import Link from "next/link";
import { getCategories } from "@/lib/mdx";
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
} from "@/components/ui/card";

export default function HomePage() {
  const categories = getCategories();

  return (
    <div className="mx-auto max-w-4xl">
      <h1 className="mb-2 text-3xl font-bold">Flashcards de Algoritmos</h1>
      <p className="mb-8 text-muted-foreground">
        Revisa os teus algoritmos de LeetCode. Escolhe uma categoria para
        começar.
      </p>
      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {categories.map((cat) => (
          <Link key={cat.slug} href={`/${cat.slug}`}>
            <Card className="h-full cursor-pointer transition-shadow hover:shadow-lg">
              <CardHeader>
                <CardTitle className="text-base">{cat.title}</CardTitle>
                <CardDescription>Categoria de algoritmos</CardDescription>
              </CardHeader>
            </Card>
          </Link>
        ))}
      </div>
    </div>
  );
}
