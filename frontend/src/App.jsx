import './App.css'

/**
 * App.jsx — Composant racine de logi_doc_pro
 *
 * Actuellement : Page d'accueil de démarrage (placeholder).
 * Prochainement : Ce composant hébergera le Router principal
 *                 avec les pages Login, Dashboard et Éditeur.
 */
function App() {
  return (
    <div className="min-h-screen bg-gray-950 flex flex-col items-center justify-center text-white font-sans">

      {/* Logo & Titre */}
      <div className="mb-8 text-center">
        <div className="inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-violet-600 mb-4 shadow-lg shadow-violet-600/30">
          <svg xmlns="http://www.w3.org/2000/svg" className="w-8 h-8 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
            <path strokeLinecap="round" strokeLinejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
          </svg>
        </div>
        <h1 className="text-4xl font-bold tracking-tight text-white">
          LogiDoc <span className="text-violet-400">Pro</span>
        </h1>
        <p className="mt-2 text-gray-400 text-lg">
          Générateur de documents professionnels avec assistance IA
        </p>
      </div>

      {/* Statut de l'environnement */}
      <div className="flex flex-col gap-3 w-full max-w-sm">
        <div className="flex items-center gap-3 bg-gray-900 border border-gray-800 rounded-xl px-4 py-3">
          <span className="w-2.5 h-2.5 rounded-full bg-green-500 flex-shrink-0 animate-pulse"></span>
          <span className="text-sm text-gray-300">Frontend React + Vite</span>
          <span className="ml-auto text-xs font-medium text-green-400">En ligne</span>
        </div>
        <div className="flex items-center gap-3 bg-gray-900 border border-gray-800 rounded-xl px-4 py-3">
          <span className="w-2.5 h-2.5 rounded-full bg-green-500 flex-shrink-0"></span>
          <span className="text-sm text-gray-300">Tailwind CSS v3</span>
          <span className="ml-auto text-xs font-medium text-green-400">Configuré</span>
        </div>
        <div className="flex items-center gap-3 bg-gray-900 border border-gray-800 rounded-xl px-4 py-3">
          <span className="w-2.5 h-2.5 rounded-full bg-green-500 flex-shrink-0"></span>
          <span className="text-sm text-gray-300">Backend Django + PostgreSQL</span>
          <span className="ml-auto text-xs font-medium text-green-400">Opérationnel</span>
        </div>
        <div className="flex items-center gap-3 bg-gray-900 border border-gray-800 rounded-xl px-4 py-3">
          <span className="w-2.5 h-2.5 rounded-full bg-yellow-500 flex-shrink-0"></span>
          <span className="text-sm text-gray-300">Module Authentification</span>
          <span className="ml-auto text-xs font-medium text-yellow-400">À venir</span>
        </div>
      </div>

      {/* Pied de page */}
      <p className="mt-10 text-xs text-gray-600">
        Phase 0 — Setup &amp; Architecture · logi_doc_pro
      </p>
    </div>
  )
}

export default App
