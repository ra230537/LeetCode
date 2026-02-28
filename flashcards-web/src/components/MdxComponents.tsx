import { RevealCard } from "./RevealCard";
import { MermaidRenderer } from "./MermaidRenderer";
import type { MDXComponents } from "mdx/types";
import type { ReactElement } from "react";

export const mdxComponents: MDXComponents = {
  blockquote: (props) => (
    <RevealCard variant="sacada">{props.children}</RevealCard>
  ),
  pre: (props) => {
    const child = props.children as ReactElement<{
      className?: string;
      children?: string;
    }>;
    if (child?.props?.className === "language-mermaid") {
      return (
        <RevealCard variant="modelo-mental">
          <MermaidRenderer chart={child.props.children?.trim() ?? ""} />
        </RevealCard>
      );
    }
    return (
      <pre
        className="overflow-x-auto rounded-lg bg-zinc-900 p-4 text-sm text-zinc-100"
        {...props}
      />
    );
  },
};
