
export type Book = {
  id: number;
  title: string;
  description: string;
  tags: string[];
  url: string; 
  type: 'markdown' | 'pdf' | 'multichapter';
  chapters?: number; // Total number of project chapters
  summary?: boolean; // Does it have a summary chapter
};

export const books: Book[] = [
  {
    id: 1,
    title: "Hacking: The Art of Exploitation",
    description: "A hands‑on, low‑level guide to offensive security that teaches exploitation from first principles — covering C, memory corruption, shellcode, debugging, and network attacks with practical examples and exercises.",
    tags: ["Exploitation", "Memory Corruption", "Shellcode", "C Programming", "Reverse Engineering", "Penetration Testing", "Classic"],
    url: "hacking-the-art-of-exploitation",
    type: 'pdf',
  },
  {
    id: 2,
    title: "The Cybersecurity Project Handbook: 32 Hands-On Projects for Offensive, Defensive & Emerging Domains",
    description: "A practical, project-driven handbook that guides learners through 32 real-world cybersecurity and blockchain projects — covering web & network pentesting, red teaming, blue-team defenses, digital forensics, cloud DDoS mitigation, secure network topology, and blockchain security proofs. Each chapter lists required skills, toolchains, and a week-by-week build plan so students and practitioners can build, test, document, and demo safe lab-ready prototypes.",
    tags: ["Cybersecurity", "VAPT", "Web Application Security", "Network Security", "Digital Forensics", "Red Teaming", "Blue Teaming", "Cloud Security", "DDoS Mitigation", "Blockchain Security", "Project-Based Learning", "Hands-on Labs"],
    url: "cybersecurity-blockchain-projects",
    type: 'multichapter',
    chapters: 32,
    summary: true,
  },
  {
    id: 3,
    title: "A Smarter Way to Learn Python",
    description: "Learn it faster. Remember it longer. A unique and effective way to learn Python, combining clear explanations with interactive online exercises. By Mark Myers.",
    tags: ["Python", "Programming", "Beginner", "Learning"],
    url: "a-smarter-way-to-learn-python",
    type: 'pdf',
  },
  {
    id: 4,
    title: "AI-Driven Cybersecurity: The Future of Digital Defense",
    description: "A comprehensive guide to understanding and applying Artificial Intelligence in both offensive and defensive cybersecurity. This book covers everything from foundational concepts to practical, hands-on projects with modern tools.",
    tags: ["AI", "Machine Learning", "Cybersecurity", "Deep Learning", "Threat Detection", "Automation"],
    url: "ai-driven-cybersecurity",
    type: 'multichapter',
    chapters: 20,
    summary: true,
  },
];
