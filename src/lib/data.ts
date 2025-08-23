// In a real app, this data would be fetched from a database.

export const blogPosts = [
  {
    id: '1',
    title: "Understanding the MITRE ATT&CK Framework",
    status: "Published",
    createdAt: "2023-10-26",
  },
  {
    id: '2',
    title: "Top 10 Cybersecurity Threats to Watch in 2024",
    status: "Published",
    createdAt: "2023-10-22",
  },
  {
    id: '3',
    title: "The Role of AI in Modern Cybersecurity",
    status: "Draft",
    createdAt: "2023-10-18",
  },
];

export const resources = [
  { id: '1', title: "OWASP Top 10", category: "Article", createdAt: "2023-10-20" },
  { id: '2', title: "Nmap", category: "Tool", createdAt: "2023-10-19" },
  { id: '3', title: "SANS Reading Room", category: "Guide", createdAt: "2023-10-18" },
];

export const feedbacks = [
    { id: '1', name: "John Doe", email: "john.doe@example.com", type: "Suggestion", message: "Great platform! Would love to see more content on IoT security.", createdAt: "2023-11-01" },
    { id: '2', name: "Jane Smith", email: "jane.smith@example.com", type: "Other", message: "The login button is not working on Firefox.", createdAt: "2023-10-31" },
    { id: '3', name: "Sam Wilson", email: "sam.wilson@example.com", type: "Compliment", message: "Your learning series is fantastic! Very well structured.", createdAt: "2023-10-30" },
];
