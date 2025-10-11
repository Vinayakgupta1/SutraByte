import { type SVGProps } from "react";

export function SutraByteLogo(props: SVGProps<SVGSVGElement>) {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 64 64"
      fill="none"
      {...props}
    >
      <title>SutraByte Logo</title>
      <circle cx="32" cy="32" r="30" fill="hsl(var(--primary))" />
      <g transform="translate(32,32)">
        <ellipse cx="0" cy="0" rx="24" ry="16" stroke="hsl(var(--primary-foreground))" strokeWidth="3" fill="none" transform="rotate(45)" />
        <ellipse cx="0" cy="0" rx="24" ry="16" stroke="hsl(var(--primary-foreground))" strokeWidth="3" fill="none" transform="rotate(-45)" />
      </g>
      <path
        d="M32 22 L38 25 L38 33 C38 40 32 44 32 44 C32 44 26 40 26 33 L26 25 Z"
        fill="hsl(var(--primary-foreground))"
      />
      <rect x="28" y="30" width="8" height="6" rx="1" fill="hsl(var(--primary))" />
      <path
        d="M30 30 V 28 A 2 2 0 0 1 34 28 V 30"
        stroke="hsl(var(--primary))"
        strokeWidth="2.5"
        fill="none"
        strokeLinecap="round"
      />
      <text
        x="32"
        y="36.5"
        fontFamily="sans-serif"
        fontSize="5"
        fill="hsl(var(--primary-foreground))"
        textAnchor="middle"
        fontWeight="bold"
      >
        म
      </text>
    </svg>
  );
}
