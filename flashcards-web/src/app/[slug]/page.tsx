import { MDXRemote } from "next-mdx-remote/rsc";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";
import { getAllSlugs, getCategoryContent, getCategories } from "@/lib/mdx";
import { mdxComponents } from "@/components/MdxComponents";

interface PageProps {
  params: Promise<{ slug: string }>;
}

export async function generateStaticParams() {
  return getAllSlugs().map((slug) => ({ slug }));
}

export async function generateMetadata({ params }: PageProps) {
  const { slug } = await params;
  const categories = getCategories();
  const cat = categories.find((c) => c.slug === slug);
  return {
    title: cat ? `${cat.title} — Flashcards` : "Flashcards",
  };
}

export default async function CategoryPage({ params }: PageProps) {
  const { slug } = await params;
  const content = getCategoryContent(slug);
  const categories = getCategories();
  const cat = categories.find((c) => c.slug === slug);

  return (
    <div className="mx-auto max-w-4xl">
      <h1 className="mb-6 text-3xl font-bold">{cat?.title ?? slug}</h1>
      <article className="prose dark:prose-invert max-w-none">
        <MDXRemote
          source={content}
          components={mdxComponents}
          options={{
            mdxOptions: {
              format: "md",
              remarkPlugins: [remarkMath],
              rehypePlugins: [rehypeKatex as never],
            },
          }}
        />
      </article>
    </div>
  );
}
