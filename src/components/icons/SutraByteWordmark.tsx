import { type SVGProps } from 'react';

export function SutraByteWordmark(props: SVGProps<SVGSVGElement>) {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 180 60"
      {...props}
    >
      <title>SutraByte Wordmark</title>
      <g className="text-primary" fill="currentColor">
        <g>
          <path
            d="M48.7,18.9H29.3c-3.1,0-5.6,2.5-5.6,5.6v18.8c0,3.1,2.5,5.6,5.6,5.6h19.4c3.1,0,5.6-2.5,5.6-5.6V24.5C54.3,21.4,51.8,18.9,48.7,18.9z"
            fill="none"
            stroke="currentColor"
            strokeWidth="3"
          />
          <path
            d="M40.8,9.4h-10c-4.4,0-8,3.6-8,8v1.5h26V17.3C48.8,13,45.2,9.4,40.8,9.4z"
            fill="none"
            stroke="currentColor"
            strokeWidth="3"
          />
          <path
            d="M39,43.3V25.5 M33.2,43.3V34.1L39,25.5 M44.8,43.3V37.6L39,25.5"
            fill="none"
            stroke="currentColor"
            strokeWidth="3"
            strokeLinecap="round"
          />
          <circle cx="39" cy="45.3" r="2" />
          <circle cx="31.6" cy="32.5" r="2" />
          <circle cx="46.4" cy="36" r="2" />
        </g>
        <text
          x="65"
          y="30"
          fontFamily="Inter, sans-serif"
          fontSize="22"
          fontWeight="bold"
        >
          Sutra
        </text>
        <text
          x="65"
          y="54"
          fontFamily="Inter, sans-serif"
          fontSize="22"
          fontWeight="bold"
        >
          Byte
        </text>
      </g>
    </svg>
  );
}
