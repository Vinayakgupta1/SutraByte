export type TryHackMeRoom = {
  id: number;
  title: string;
  difficulty: 'Easy' | 'Medium' | 'Hard';
  tags: string[];
  url: string;
  completed: boolean;
  locked: boolean;
  blogUrl?: string;
  videoUrl?: string;
};

export const tryHackMeRooms: TryHackMeRoom[] = [
  {
    id: 1,
    title: 'Metasploit Home Lab : Full Kill Chain',
    difficulty: 'Medium',
    tags: ['Kill Chain', 'Metasploit', 'Home Lab'],
    url: 'https://tryhackme.com/jr/metasploithomelabfullkillchain',
    completed: true,
    locked: false,
    blogUrl: 'https://vinayak15.medium.com/metasploit-walkthrough-cyber-kill-chain-in-action-12bbe5d698aa',
    videoUrl: 'https://youtu.be/TzvXgcHu2gM',
  },
  {
    id: 2,
    title: 'ISC2 CC - Theory Walkthrough Lab',
    difficulty: 'Medium',
    tags: ['ISC2CC', 'CIA Triad'],
    url: 'https://tryhackme.com/jr/isc2cctheorywalkthroughlab',
    completed: true,
    locked: false,
    blogUrl: 'https://vinayak15.medium.com/%EF%B8%8F-isc2-cc-theory-walkthrough-lab-complete-guide-with-q-a-a02a4d0d18c7',
  },
  {
    id: 3,
    title: 'CyberForge 180',
    difficulty: 'Medium',
    tags: ['CyberSecurity Enginner Roadmap', '6-Months Roadmap'],
    url: 'https://tryhackme.com/jr/cyberforge180',
    completed: true,
    locked: false,
    blogUrl: 'https://medium.com/@vinayak15/cyberforge-180-tryhackme-room-walkthrough-2bc7350935dd',
  },
  {
    id: 4,
    title: 'Pickle Rick',
    difficulty: 'Easy',
    tags: ['Web', 'Command Injection'],
    url: 'https://tryhackme.com/room/picklerick',
    completed: false,
    locked: true,
  },
    {
    id: 5,
    title: 'Mr. Robot CTF',
    difficulty: 'Medium',
    tags: ['Web', 'WordPress', 'Privilege Escalation'],
    url: 'https://tryhackme.com/room/mrrobot',
    completed: false,
    locked: true,
  },
   {
    id: 6,
    title: 'RootMe',
    difficulty: 'Easy',
    tags: ['Linux', 'Privilege Escalation', 'SUID'],
    url: 'https://tryhackme.com/room/rrootme',
    completed: false,
    locked: true,
  },
];
