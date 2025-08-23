export type BlogPost = {
  title: string;
  excerpt: string;
  date: string;
  tags: string[];
  url: string;
  aiHint: string;
};

export const blogPosts: BlogPost[] = [
  {
    title: "Linux File Systems Beginner's Guide",
    excerpt: "A Beginner's Journey into Linux File Systems 🚀",
    date: "September 27, 2024",
    tags: ["Linux", "File Systems", "Beginners"],
    url: "https://vinayak15.medium.com/a-beginners-journey-into-linux-file-systems-e9ef8c665d5a",
    aiHint: "linux file system"
  },
  {
    title: "Function Calling in AI: A Game Changer",
    excerpt: "🤖 Building an AI Study Buddy with Function Calling",
    date: "April 5, 2025",
    tags: ["AI", "Innovation"],
    url: "https://vinayak15.medium.com/building-an-ai-study-buddy-with-function-calling-bd923a6a90ef",
    aiHint: "artificial intelligence"
  },
];
