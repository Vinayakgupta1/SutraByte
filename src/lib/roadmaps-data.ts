export type Roadmap = {
  id: number;
  title: string;
  description: string;
  tags: string[];
  url: string; 
  type: 'markdown' | 'pdf';
};

export const roadmaps: Roadmap[] = [
  {
    id: 1,
    title: "180 Days Cybersecurity Engineer Roadmap",
    description: "A comprehensive 180-day guide to becoming a Cybersecurity Engineer, covering foundational knowledge to advanced skills.",
    tags: ["Cybersecurity", "Roadmap", "Career", "Learning Plan"],
    url: "180-days-cybersecurity-engineer-roadmap",
    type: 'markdown',
  },
  {
    id: 2,
    title: "90 Days Cybersecurity Learning Roadmap",
    description: "A focused 90-day plan for learning the essentials of cybersecurity. Learn it faster. Remember it longer.",
    tags: ["Cybersecurity", "Roadmap", "Learning Plan", "Beginner"],
    url: "90-days-cybersecurity-roadmap",
    type: 'pdf',
  },
];
