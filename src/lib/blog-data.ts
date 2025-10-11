export type BlogPost = {
	title: string;
	excerpt: string;
	tags: string[];
	date: string;
	url: string;
};

export const blogPosts: BlogPost[] = [
	{
		title: "Getting Started with Cybersecurity Labs",
		excerpt: "A beginner-friendly walkthrough to set up your environment and start practicing.",
		tags: ["Beginner", "Labs", "Guide"],
		date: "2025-01-10",
		url: "https://sutrabyte.com/blog/getting-started-cyber-labs",
	},
	{
		title: "Understanding Common Vulnerabilities: XSS, SQLi, and More",
		excerpt: "An overview of common web vulnerabilities with examples and mitigation tips.",
		tags: ["Web", "Vulnerabilities", "OWASP"],
		date: "2025-02-02",
		url: "https://sutrabyte.com/blog/common-vulnerabilities-overview",
	},
	{
		title: "Practical Network Security: Tools and Techniques",
		excerpt: "Hands-on techniques and tooling to assess and secure networks effectively.",
		tags: ["Networking", "Tools", "Guides"],
		date: "2025-03-15",
		url: "https://sutrabyte.com/blog/practical-network-security",
	},
];
