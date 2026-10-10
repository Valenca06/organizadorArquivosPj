# 📁 Organizador Inteligente de Arquivos & Detector de Duplicatas

Um utilitário em Python leve, rápido e sem dependências externas, projetado para organizar diretórios, identificar arquivos idênticos por impressão digital (MD5) e categorizá-los em subpastas por extensão.

---

## 🚀 Recursos Principais

- **Detecta duplicatas por Hash MD5**: Compara o conteúdo binário real do arquivo. Se dois arquivos tiverem nomes diferentes, mas conteúdos idênticos, o programa detectará a duplicata.
- **Interação Segura**: Exibe o arquivo original, lista todas as cópias encontradas e pergunta ao usuário se deseja apagar **todas de uma vez** ou **selecionar uma por uma**.
- **Categorização Automática**: Move os arquivos restantes para subpastas dedicadas (`Imagens`, `PDFs`, `Documentos`, `Videos`, `Audios`, `Compactados`, `Outros`).
- **Autopreservação**: Ignora o próprio script (`.py`) durante a movimentação para não afetar a execução.
- **Zero Dependências de Terceiros**: Desenvolvido exclusivamente com a biblioteca padrão do Python.

---

## 🔍 Como Funciona a Detecção por Hash MD5?

Comparar apenas o nome do arquivo não é confiável (ex: `relatorio.txt` e `relatorio(1).txt` podem ser o mesmo arquivo, enquanto dois arquivos chamados `dados.csv` em pastas diferentes podem conter dados completamente distintos).

Para resolver isso, o `main.py` lê o conteúdo binário de cada arquivo e gera um **hash MD5** (uma assinatura única de 32 caracteres hexadecimais).

1. **Mapeamento**: O script lê todos os arquivos do diretório atual e agrupa os caminhos de cada arquivo usando o hash MD5 como chave.
2. **Identificação**: Qualquer grupo de hash que contenha mais de um arquivo é classificado como duplicata exata.
3. **Decisão do Usuário**: O primeiro arquivo mapeado é mantido como **Original**, e as cópias subsequentes são listadas para confirmação de remoção (`d.unlink()`).

---

## 🗂️ Estrutura de Categorização

Após o tratamento das duplicatas, o script mapeia as extensões restantes e organiza os arquivos nas seguintes pastas:

| Categoria | Extensões Suportadas |
| :--- | :--- |
| **Imagens** | `.jpg`, `.jpeg`, `.png`, `.gif` |
| **PDFs** | `.pdf` |
| **Documentos** | `.docx`, `.txt`, `.xlsx`, `.csv` |
| **Compactados**| `.zip`, `.rar`, `.7z` |
| **Vídeos** | `.mp4`, `.mkv` |
| **Áudios** | `.mp3`, `.wav` |
| **Outros** | Qualquer extensão não listada acima |

---

## 🔬 Testes e Validação de Integridade (`test.py`)

Para garantir que a organização ocorreu de forma precisa e sem perda ou corrupção de dados, o projeto inclui um script de validação automatizada (**`test.py`**).

Ele atua como uma verificação pós-execução sobre o diretório organizado.

---

### 🎯 O que o `test.py` verifica?

- **Ausência de Duplicatas Restantes**: Varre recursivamente o diretório e calcula os hashes MD5 para confirmar que nenhum arquivo idêntico permaneceu duplicado.
- **Precisão do Mapeamento**: Confirma se cada arquivo foi alocado na subpasta correspondente à sua extensão (ex: `.pdf` dentro de `PDFs/`, `.jpg` dentro de `Imagens/`).
- **Arquivos Desconhecidos**: Garante que arquivos com extensões não categorizadas foram movidos corretamente para a pasta `Outros/`.
- **Contagem de Preservação**: Compara o total de arquivos originais esperados com o total final para assegurar que nenhum arquivo legítimo foi apagado acidentalmente.

---

## 🔄 Fluxo Completo de Testes

Para executar o ciclo completo de validação do projeto (geração, execução e teste):

1. **Criar o ambiente limpo de testes**:
   ```bash
   python gen.py

## 💻 Como Executar

Abra o terminal no diretório onde os arquivos estão localizados e execute o script principal nele (lembre-se de mover o script principal pra dentro da pasta a ser orgnizada):

```bash
python main.py

---