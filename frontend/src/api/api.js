import axios from 'axios';

const API = axios.create({
  baseURL: 'https://skill-graph.onrender.com/apis',
  headers: { 'Content-Type': 'application/json' },
});

// ── User APIs ──────────────────────────────────────────────

export const registerUser = (name, email, password) =>
  API.post('/user/register', { name, email, password });

export const loginUser = (email, password) =>
  API.post('/user/login', { email, password });

export const createUser = (data) =>
  API.post('/user/create', data);

export const getUserInfo = (id) =>
  API.get('/user/info/', { params: { id } });

export const setUserObjective = (userId, careerId) =>
  API.post('/user/objective', { user_id: userId, career_id: careerId });

export const updateUserCareer = (userId, careerId) =>
  API.post('/user/career/update', { user: userId, career: careerId });

export const getUserNeeds = (id) =>
  API.get('/user/need', { params: { id } });

export const getLearningPath = (id) =>
  API.get('/user/learning-path', { params: { id } });

export const getLearningPathInfo = (courses, userId) =>
  API.post('/user/lp', { courses, user: userId });

// ── Learning Object (skill) APIs ───────────────────────────

export const getUserSkills = (id) =>
  API.get('/user/has', { params: { id } });

export const submitUserSkills = (userId, listLo) =>
  API.post('/user/has', { user_id: userId, list_lo: listLo });

export const addUserSkill = (userId, loId, level) =>
  API.post('/user/has/create', { user: userId, lo: loId, level });

export const removeUserSkill = (userId, loId) =>
  API.post('/user/has/delete', { user: userId, lo: loId });

export const getLanguages = () => API.get('/lo/language/');
export const getKnowledge = () => API.get('/lo/knowledge');
export const getTools = () => API.get('/lo/tool');
export const getPlatforms = () => API.get('/lo/platform');
export const getFrameworks = () => API.get('/lo/framework');
export const searchLearningObjects = (value) =>
  API.get('/lo/all', { params: { value } });

// ── Career APIs ────────────────────────────────────────────

export const getAllCareers = () => API.get('/career/');
export const getCareerById = (id) =>
  API.get('/career/one', { params: { id } });
export const getCareerLOs = (id) =>
  API.get('/career/lo', { params: { id } });

// ── Skill Learning Path API ────────────────────────────────

export const getSkillLearningPath = (careerId) =>
  API.get('/learning-path', { params: { id: careerId } });

// ── Course APIs ────────────────────────────────────────────

export const getCourseInfo = (id) =>
  API.get('/course', { params: { id } });
export const getCourseProvidedLOs = (id) =>
  API.get('/course/provided/lo', { params: { id } });
export const getCourseRequiredLOs = (id) =>
  API.get('/course/required/lo', { params: { id } });

// ── Health ─────────────────────────────────────────────────

export const healthCheck = () => API.get('/health/');

// ── Chatbot API ─────────────────────────────────────────────

export const chatWithTutor = (messages) =>
  API.post('/chatbot/chat', { messages });
