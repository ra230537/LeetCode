import fs from "fs";
import path from "path";

const CONTENT_DIR = path.join(process.cwd(), "content");

export interface CategoryMeta {
  slug: string;
  title: string;
}

export function getCategories(): CategoryMeta[] {
  const files = fs.readdirSync(CONTENT_DIR).filter((f) => f.endsWith(".md"));
  return files.map((file) => {
    const slug = file.replace(/\.md$/, "");
    const title = slug
      .split(/[-_]/)
      .map((w) => w.charAt(0).toUpperCase() + w.slice(1))
      .join(" ");
    return { slug, title };
  });
}

export function getCategoryContent(slug: string): string {
  const filePath = path.join(CONTENT_DIR, `${slug}.md`);
  return fs.readFileSync(filePath, "utf-8");
}

export function getAllSlugs(): string[] {
  return getCategories().map((c) => c.slug);
}
