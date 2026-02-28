"use client";

import { useState, type ReactNode } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Lightbulb, Brain, ChevronRight, ChevronDown } from "lucide-react";

interface RevealCardProps {
  children: ReactNode;
  variant?: "sacada" | "modelo-mental";
  label?: string;
}

const variantConfig = {
  sacada: {
    icon: Lightbulb,
    defaultLabel: "Clica para revelar a Sacada",
    borderClass: "border-yellow-500/30",
    bgClass: "bg-yellow-500/5",
    iconClass: "text-yellow-600 dark:text-yellow-500",
  },
  "modelo-mental": {
    icon: Brain,
    defaultLabel: "Clica para revelar o Modelo Mental",
    borderClass: "border-blue-500/30",
    bgClass: "bg-blue-500/5",
    iconClass: "text-blue-600 dark:text-blue-500",
  },
};

export function RevealCard({
  children,
  variant = "sacada",
  label,
}: RevealCardProps) {
  const [revealed, setRevealed] = useState(false);
  const config = variantConfig[variant];
  const Icon = config.icon;
  const displayLabel = label ?? config.defaultLabel;

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" || e.key === " ") {
      e.preventDefault();
      setRevealed((prev) => !prev);
    }
  };

  return (
    <Card
      role="button"
      tabIndex={0}
      aria-expanded={revealed}
      className={`my-4 cursor-pointer border-dashed border-2 transition-all hover:shadow-md ${config.borderClass} ${config.bgClass}`}
      onClick={() => setRevealed((prev) => !prev)}
      onKeyDown={handleKeyDown}
    >
      <CardContent className="p-4">
        {revealed ? (
          <div>
            <div
              className={`mb-3 flex items-center gap-2 font-medium ${config.iconClass}`}
            >
              <Icon className="size-4 shrink-0" aria-hidden />
              <span>{displayLabel.replace(/^Clica para revelar (a|o) /, "")}</span>
              <ChevronDown className="ml-auto size-4 shrink-0" aria-hidden />
            </div>
            <div className="prose dark:prose-invert max-w-none">{children}</div>
          </div>
        ) : (
          <div className="flex items-center justify-center gap-2 text-muted-foreground">
            <Icon className={`size-5 shrink-0 ${config.iconClass}`} aria-hidden />
            <p className="font-medium">{displayLabel}</p>
            <ChevronRight className="size-4 shrink-0" aria-hidden />
          </div>
        )}
      </CardContent>
    </Card>
  );
}
